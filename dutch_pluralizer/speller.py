import inspect
import os
from pathlib import Path

from hunspell import Hunspell

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

    dictionary_path = __resolve_path("../dict/")
    h_nl = Hunspell("nl-nl", hunspell_data_dir=str(dictionary_path))

    # add words that are not present in current dictionary
    for list in [get_plural_nouns(), get_basic_words()]:
        for word in list:
            if not h_nl.spell(word):
                h_nl.add(word)

    h_nl.clear_cache()
    h_loaded = True

    return h_nl
