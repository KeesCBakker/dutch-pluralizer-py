from typing import Tuple

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
                            
from .mapping import NounMap

__possible_plural_endings = create_ends_with_regex(
    "en", 
    # heden
    "'s",
    "s",
    "ën",
    "a",
    "i"
)


def could_be_plural(plural: str, ending_overrides: NounMap = None) -> bool:
    if __possible_plural_endings.search(plural):
        return True
    
    if ending_overrides:
        for key in ending_overrides.get_singular_map():
            if plural.endswith(key):
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


class AdvancedSingularizationResult:

    def __init__(
        self,
        algorithic_singular: [str],
        singular: str,
        suggestions: Tuple[str],
        hunspell_spelled: bool,
        could_be_plural: bool,
    ):
        self.algorithic_singular = algorithic_singular
        self.singular = singular
        self.suggestions = suggestions
        self.hunspell_spelled = hunspell_spelled
        self.could_be_plural = could_be_plural


def singularize_advanced(plural: str, speller: Hunspell = None, ending_overrides: NounMap = None) -> AdvancedSingularizationResult:

    if not could_be_plural(plural, ending_overrides):
        return AdvancedSingularizationResult(None, None, (), False, False)

    options = __process_methods(
        plural,
        lambda l: singularize_by_hard_map(l, ending_overrides), # should always be first!
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

    # debug
    # print("options", options)
    
    if not speller:
        speller = ensure_hunspell_nl()

    stems = __stem(speller, plural)

    # return option that is spelled correct
    for option in options:
        if speller.spell(option):
            return AdvancedSingularizationResult(options, option, (), True, True)

    stems = __stem(speller, plural)

    # debug
    # print("options", options, "stems", stems)

    if stems:
        return AdvancedSingularizationResult(options, stems[0], stems, True, True)

    if plural.endswith("s"):
        singular = plural[0:-1]
        if speller.spell(singular):
            return AdvancedSingularizationResult(options, singular, stems, True, True)
        else:
            # just add it a possible option
            options.append(singular)
            return AdvancedSingularizationResult(options, None, stems, False, True)

    if plural.endswith("en"):
        singular = plural[0:-2]

        if singular.endswith("v"):
            singular = singular[0:-1] + "f"
        elif singular.endswith("z"):
            singular = singular[0:-1] + "s"

        if speller.spell(singular):
            return AdvancedSingularizationResult(options, singular, stems, True, True)
        else:
            # just add it a possible option
            options.append(singular)
            return AdvancedSingularizationResult(options, None, stems, False, True)

    return AdvancedSingularizationResult(options, None, stems, False, True)


def singularize(plural: str, speller: Hunspell = None, ending_overrides: NounMap = None) -> str:
    return singularize_advanced(plural, speller, ending_overrides).singular
