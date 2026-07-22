import ctypes.util
import os
from pathlib import Path

from cffi import FFI


ffi = FFI()
ffi.cdef("""
    void* Hunspell_create(const char* affpath, const char* dpath);
    void Hunspell_destroy(void* pHunspell);
    int Hunspell_spell(void* pHunspell, const char* word);
    int Hunspell_suggest(void* pHunspell, void* slst, const char* word);
    int Hunspell_stem(void* pHunspell, void* slst, const char* word);
    int Hunspell_add(void* pHunspell, const char* word);
    int Hunspell_add_with_affix(void* pHunspell, const char* word, const char* example);
    void Hunspell_free_list(void* pHunspell, void* slst, int n);
    const char* Hunspell_get_dic_encoding(void* pHunspell);
""")

_lib_hunspell = None


def _get_hunspell_lib():
    global _lib_hunspell
    if _lib_hunspell is not None:
        return _lib_hunspell

    for name in ['hunspell-1.7', 'hunspell', 'libhunspell-1.7', 'libhunspell']:
        path = ctypes.util.find_library(name)
        if path:
            _lib_hunspell = ffi.dlopen(path)
            return _lib_hunspell

    for p in [
        '/usr/lib/x86_64-linux-gnu/libhunspell-1.7.so',
        '/usr/lib/libhunspell-1.7.so',
        '/usr/local/lib/libhunspell-1.7.so',
    ]:
        if Path(p).exists():
            _lib_hunspell = ffi.dlopen(p)
            return _lib_hunspell

    raise ImportError(
        "libhunspell not found. Install it with: "
        "apt-get install libhunspell-dev  (Linux) or "
        "brew install hunspell  (macOS)"
    )


class Hunspell:

    def __init__(self, lang='en_US', hunspell_data_dir=None):
        if hunspell_data_dir is None:
            hunspell_data_dir = os.environ.get("HUNSPELL_DATA", "")

        aff_path = os.path.join(hunspell_data_dir, f"{lang}.aff")
        dic_path = os.path.join(hunspell_data_dir, f"{lang}.dic")

        if not Path(aff_path).is_file():
            raise FileNotFoundError(f"Affix file not found: {aff_path}")
        if not Path(dic_path).is_file():
            raise FileNotFoundError(f"Dictionary file not found: {dic_path}")

        lib = _get_hunspell_lib()

        self._handle = lib.Hunspell_create(
            aff_path.encode('utf-8'),
            dic_path.encode('utf-8')
        )
        if not self._handle:
            raise MemoryError("Failed to create Hunspell instance")

        self._spell = lib.Hunspell_spell
        self._suggest = lib.Hunspell_suggest
        self._stem = lib.Hunspell_stem
        self._add = lib.Hunspell_add
        self._add_with_affix = lib.Hunspell_add_with_affix
        self._free_list = lib.Hunspell_free_list
        self._destroy = lib.Hunspell_destroy

        self._suggest_cache = {}
        self._stem_cache = {}

        enc = lib.Hunspell_get_dic_encoding(self._handle)
        self._encoding = ffi.string(enc).decode('utf-8') if enc else 'ISO8859-1'

    def __del__(self):
        if hasattr(self, '_handle') and self._handle:
            self._destroy(self._handle)

    def spell(self, word):
        return self._spell(self._handle, word.encode(self._encoding, 'ignore')) != 0

    def _string_array(self, func, free, word):
        w = word.encode(self._encoding, 'ignore')
        slst = ffi.new("char*[]", [ffi.NULL])
        count = func(self._handle, slst, w)
        try:
            if count and slst[0]:
                arr = ffi.cast("char**", slst[0])
                return tuple(
                    ffi.string(arr[i]).decode(self._encoding, 'ignore')
                    for i in range(count)
                )
            return ()
        finally:
            if count:
                free(self._handle, slst, count)

    def suggest(self, word):
        cached = self._suggest_cache.get(word)
        if cached is not None:
            return cached
        result = self._string_array(self._suggest, self._free_list, word)
        self._suggest_cache[word] = result
        return result

    def stem(self, word):
        cached = self._stem_cache.get(word)
        if cached is not None:
            return cached
        result = self._string_array(self._stem, self._free_list, word)
        self._stem_cache[word] = result
        return result

    def add(self, word, example=None):
        w = word.encode(self._encoding, 'ignore')
        if example:
            ex = example.encode(self._encoding, 'ignore')
            return self._add_with_affix(self._handle, w, ex) == 0
        return self._add(self._handle, w) == 0


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
