from hunspell import Hunspell

from .pluralizer import pluralize
from .speller import ensure_hunspell_nl
from .strategies.helpers import VOWELS, create_ends_with_regex
from .strategies.pluralize_by_hard_map import singularize_by_hard_map
from .strategies.pluralize_by_latin import singularize_by_latin
from .strategies.pluralize_eren import singularize_eren
from .strategies.pluralize_with_en import (
    singularize_with_en_double_consonant, singularize_with_en_double_vowel,
    singularize_with_en_single_vowel, singularize_with_trema_en)
from .strategies.pluralize_with_s import singularize_with_s
from .strategies.simple import (singularize_heid, singularize_jes,
                                singularize_oren)

__possible_plural_endings = create_ends_with_regex(
    "en", 
    # heden
    "'s",
    "s",
    "ën",
    "a",
    "i"
)


def could_be_plural(plural: str) -> bool:
    if __possible_plural_endings.search(plural):
        return True
    return False


def __process_methods(plural: str, *args) -> [str]:

    options = list()
    for method in args:
        x = method(plural)
        if x:
            options.append(x)

    return options


def __stem(speller: Hunspell, plural:str) -> [str]:

    stems = list()
    for stem in speller.stem(plural):
        stem = stem.replace("ĳ", "ij")
        if len(plural) - len(stem) <= 3:
            ps = pluralize(stem)
            if ps == plural:
                stems.append(stem)

    return stems


def singularize(plural: str, speller: Hunspell = None) -> str:

    if not could_be_plural(plural):
        return None

    options = __process_methods(
        plural,
        singularize_by_hard_map, # should always be first!
        singularize_oren,
        singularize_heid,
        singularize_eren,
        singularize_jes,
        singularize_by_latin,
        singularize_with_s,
        singularize_with_trema_en,
        singularize_with_en_single_vowel,
        singularize_with_en_double_vowel,
        singularize_with_en_double_consonant
    )
    
    if not speller:
        speller = ensure_hunspell_nl()

    stems = __stem(speller, plural)


    # return option that is spelled correct
    for option in options:
        if speller.spell(option):
            return option

    stems = __stem(speller, plural)

    # debug
    # print("options", options, "stems", stems)

    if stems:
        print(stems)
        return stems[0]

    if plural.endswith("s"):
        singular = plural[0:-1]
        if speller.spell(singular):
            return singular

    if plural.endswith("en"):
        singular = plural[0:-2]

        if singular.endswith("v"):
            singular = singular[0:-1] + "f"
        elif singular.endswith("z"):
            singular = singular[0:-1] + "s"

        if speller.spell(singular):
            return singular


    return None
