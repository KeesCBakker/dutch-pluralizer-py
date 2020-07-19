import re
from typing import Tuple

from hunspell import Hunspell

from .mapping import NounEndingMap
from .replacements import (SearchResult, search_by_dictionary,
                           search_by_dictionary_plus_s, search_by_suggestions)
from .speller import ensure_hunspell_nl, get_plural_nouns
from .strategies.pluralize_bastard import pluralize_bastard
from .strategies.pluralize_by_hard_map import pluralize_by_hard_map
from .strategies.pluralize_by_latin import pluralize_by_latin
from .strategies.pluralize_eren import pluralize_eren
from .strategies.pluralize_long_vowel import pluralize_long_vowel
from .strategies.pluralize_man import pluralize_man
from .strategies.pluralize_oren import pluralize_oren
from .strategies.pluralize_with_en import pluralize_with_en
from .strategies.pluralize_with_s import pluralize_with_s


class AdvancedPluralizationResult:

    def __init__(
        self,
        algorithmic_plural: str,
        plural: str,
        suggestions: Tuple[str],
        switched_ending_from: str,
        switched_ending_to: str,
        hunspell_spelled: bool
    ):
        self.algorithmic_plural = algorithmic_plural
        self.plural = plural
        self.suggestions = suggestions
        self.switched_ending_from = switched_ending_from
        self.switched_ending_to = switched_ending_to
        self.hunspell_spelled = hunspell_spelled


def __pluralize(singular: str, ending_overrides: NounEndingMap = None) -> str:
    return \
        pluralize_by_hard_map(singular, ending_overrides) or \
        pluralize_eren(singular) or \
        pluralize_oren(singular) or \
        pluralize_man(singular) or \
        pluralize_by_latin(singular) or \
        pluralize_long_vowel(singular) or \
        pluralize_bastard(singular) or \
        pluralize_with_s(singular) or \
        pluralize_with_en(singular) or \
        None


def pluralize_advanced(singular: str, speller: Hunspell = None, ending_overrides: NounEndingMap = None) -> AdvancedPluralizationResult:

    if not speller:
        speller = ensure_hunspell_nl()

    plural = __pluralize(singular, ending_overrides)

    # empty plural - just stop
    if not plural:
        return AdvancedPluralizationResult(plural, None, (), None, None, False)

    # right spelled plural
    if speller.spell(plural):
        return AdvancedPluralizationResult(plural, plural, (), None, None, True)

    # if no rightly spelled word can be found, use suggestions,
    # replacement of the endings and the Hunspell dictionary if
    # we can find something that is spelled correctly.
    suggestions = speller.suggest(plural)
    search_result:SearchResult = \
        search_by_suggestions(plural, suggestions) or \
        search_by_dictionary(speller, plural) or \
        search_by_dictionary_plus_s(speller, singular)
    
    if search_result:
        return AdvancedPluralizationResult(
            plural,
            search_result.plural,
            suggestions,
            search_result.switched_ending_from,
            search_result.switched_ending_to,
            True
        )

    return AdvancedPluralizationResult(plural, None, (), None, None, False)


def pluralize(singular: str, speller: Hunspell = None, ending_overrides: NounEndingMap = None) -> str:
    result = pluralize_advanced(singular, speller, ending_overrides)
    return result.plural
