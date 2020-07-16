# Yeah, sometimes is is too hard to do it algoritmically, or I'm
# just way too lazy, so here is a map for all those silly exceptions
# that we like to have in Dutch.
# Other words that end up here have plurals that are excepted by
# Hunspell, but not on VanDale.nl

from ..mapping import NounEndingMap

__hard_map = NounEndingMap({
    "gelid": "gelederen",
    "lid": "leden",
    "schip": "schepen",
    "stad": "steden",
    "infuus": "infusen",
    "lelie": "lelies",
    "oom": "ooms",
    "bruidegom": "bruidegoms",
    "serum": "serums",
    "make-up": "make-ups",
    "glas": "glazen",
    "graf": "graven",  # added case for singlar
    "bh": "bh's",
})

__only_for_singularize = NounEndingMap({
    "ine": "inen"
})


def pluralize_by_hard_map(singular: str, overrides: NounEndingMap) -> str:

    for nouns in [overrides, __hard_map]:
        if nouns:
            plural = nouns.pluralize_by_endings(singular)
            if plural:
                return plural

    return None


def singularize_by_hard_map(plural: str, overrides: NounEndingMap) -> str:

    for nouns in [overrides, __hard_map, __only_for_singularize]:
        if nouns:
            singular = nouns.singularize_by_endings(plural)
            if singular:
                return singular

    return None

