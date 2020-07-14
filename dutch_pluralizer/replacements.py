from typing import Tuple, Union
from hunspell import Hunspell

__ending_pairs = [{
    "sen": "zen",
    "zen": "sen",
    "des": "den",
    "den": "des",
    "iën": "ieën",
    "ieën": "iën",
    "a": "ums",
    "i": "ussen"
}]


class SearchResult:
    def __init__(self, plural: str, switched_ending_from: str, switched_ending_to: str):
        self.plural = plural
        self.switched_ending_from = switched_ending_from
        self.switched_ending_to = switched_ending_to


def check_switch_ending(e1, e2, plural, suggestions):
    if plural.endswith(e1):
        plural = plural[0:0-len(e1)] + e2
        if plural in suggestions:
            return plural
    return None


def search_by_suggestions(plural:str, suggestions: Tuple[str]) -> Union[None, SearchResult]:
    for e in __ending_pairs:
        for key in e.keys():
            x = check_switch_ending(key, e[key], plural, suggestions)
            if x:
                return SearchResult(x, key, e[key])
                
    return None


def search_by_dictionary(speller:Hunspell, plural: str) -> Union[None, SearchResult]:
    for e in __ending_pairs:
        for key in e.keys():
            if plural.endswith(key):
                suggestion = plural[0:0-len(key)] + e[key]
                if speller.spell(suggestion):
                    return SearchResult(suggestion, key, e[key])

    return None


def search_by_dictionary_plus_s(speller: Hunspell, singular: str) -> Union[None, SearchResult]:

    plural = singular + 's'

    if speller.spell(plural):
        return SearchResult(plural, None,"s")

    return None
