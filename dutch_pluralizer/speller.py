import ctypes
import ctypes.util
import inspect
import os
from pathlib import Path


class Hunspell:
    _lib = None

    @classmethod
    def _get_lib(cls):
        if cls._lib is not None:
            return cls._lib

        for name in ['hunspell-1.7', 'hunspell', 'libhunspell-1.7', 'libhunspell']:
            path = ctypes.util.find_library(name)
            if path:
                cls._lib = ctypes.CDLL(path)
                break

        if cls._lib is None:
            for p in [
                '/usr/lib/x86_64-linux-gnu/libhunspell-1.7.so',
                '/usr/lib/libhunspell-1.7.so',
                '/usr/local/lib/libhunspell-1.7.so',
            ]:
                if Path(p).exists():
                    cls._lib = ctypes.CDLL(p)
                    break

        if cls._lib is None:
            raise ImportError(
                "libhunspell not found. Install it with: "
                "apt-get install libhunspell-dev  (Linux) or "
                "brew install hunspell  (macOS)"
            )

        cls._setup_funcs()
        return cls._lib

    @classmethod
    def _setup_funcs(cls):
        lib = cls._lib

        lib.Hunspell_create.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        lib.Hunspell_create.restype = ctypes.c_void_p

        lib.Hunspell_destroy.argtypes = [ctypes.c_void_p]
        lib.Hunspell_destroy.restype = None

        lib.Hunspell_spell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.Hunspell_spell.restype = ctypes.c_int

        lib.Hunspell_suggest.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
            ctypes.c_char_p,
        ]
        lib.Hunspell_suggest.restype = ctypes.c_int

        lib.Hunspell_stem.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
            ctypes.c_char_p,
        ]
        lib.Hunspell_stem.restype = ctypes.c_int

        lib.Hunspell_add.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.Hunspell_add.restype = ctypes.c_int

        lib.Hunspell_add_with_affix.argtypes = [
            ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
        lib.Hunspell_add_with_affix.restype = ctypes.c_int

        lib.Hunspell_free_list.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
            ctypes.c_int,
        ]
        lib.Hunspell_free_list.restype = None

        lib.Hunspell_get_dic_encoding.argtypes = [ctypes.c_void_p]
        lib.Hunspell_get_dic_encoding.restype = ctypes.c_char_p

    def __init__(self, lang='en_US', hunspell_data_dir=None):
        if hunspell_data_dir is None:
            hunspell_data_dir = os.environ.get("HUNSPELL_DATA", "")

        aff_path = os.path.join(hunspell_data_dir, f"{lang}.aff")
        dic_path = os.path.join(hunspell_data_dir, f"{lang}.dic")

        if not Path(aff_path).is_file():
            raise FileNotFoundError(f"Affix file not found: {aff_path}")
        if not Path(dic_path).is_file():
            raise FileNotFoundError(f"Dictionary file not found: {dic_path}")

        lib = self._get_lib()
        self._handle = lib.Hunspell_create(
            aff_path.encode('utf-8'),
            dic_path.encode('utf-8')
        )
        if not self._handle:
            raise MemoryError("Failed to create Hunspell instance")

        enc = lib.Hunspell_get_dic_encoding(self._handle)
        self._encoding = enc.decode('utf-8') if enc else 'ISO8859-1'

    def __del__(self):
        if hasattr(self, '_handle') and self._handle:
            self._get_lib().Hunspell_destroy(self._handle)

    def _translate(self, items, count):
        return tuple(
            items[i].decode(self._encoding, 'ignore')
            for i in range(count)
        )

    def spell(self, word):
        return self._get_lib().Hunspell_spell(
            self._handle, word.encode(self._encoding, 'ignore')
        ) != 0

    def suggest(self, word):
        lib = self._get_lib()
        w = word.encode(self._encoding, 'ignore')
        arr = ctypes.POINTER(ctypes.c_char_p)()
        count = lib.Hunspell_suggest(self._handle, ctypes.byref(arr), w)
        try:
            return self._translate(arr, count)
        finally:
            if count:
                lib.Hunspell_free_list(self._handle, ctypes.byref(arr), count)

    def stem(self, word):
        lib = self._get_lib()
        w = word.encode(self._encoding, 'ignore')
        arr = ctypes.POINTER(ctypes.c_char_p)()
        count = lib.Hunspell_stem(self._handle, ctypes.byref(arr), w)
        try:
            return self._translate(arr, count)
        finally:
            if count:
                lib.Hunspell_free_list(self._handle, ctypes.byref(arr), count)

    def add(self, word, example=None):
        lib = self._get_lib()
        w = word.encode(self._encoding, 'ignore')
        if example:
            ex = example.encode(self._encoding, 'ignore')
            return lib.Hunspell_add_with_affix(self._handle, w, ex) == 0
        return lib.Hunspell_add(self._handle, w) == 0


h_nl = None
h_loaded = False


def __resolve_path(sub: str) -> str:
    base_path = Path(__resolve_path.__code__.co_filename)
    path = (base_path / sub).resolve()
    return str(path)


def __read_relative_path(sub: str)-> [str]:
    file = __resolve_path(sub)
    with open(file, encoding="utf-8-sig") as f:
        return f.read().splitlines()


def get_plural_nouns() -> [str]:
    return __read_relative_path("../dict/nouns-meervouden.txt")


def get_basic_words() -> [str]:
    return __read_relative_path("../dict/basiswoorden-gekeurd.txt")


def ensure_hunspell_nl() -> Hunspell:
    global h_nl
    global h_loaded
    if h_loaded:
        return h_nl
    h_nl = new_hunspell_nl()
    h_loaded = True
    return h_nl


def new_hunspell_nl() -> Hunspell:
    dictionary_path = __resolve_path("../dict/")
    hnspl = Hunspell("nl-nl", hunspell_data_dir=str(dictionary_path))
    for lst in [get_plural_nouns(), get_basic_words()]:
        for word in lst:
            hnspl.add(word)
    return hnspl
