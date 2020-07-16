# Yeah, sometimes is is too hard to do it algoritmically, or I'm
# just way too lazy, so here is a map for all those silly exceptions
# that we like to have in Dutch.
# Other words that end up here have plurals that are excepted by
# Hunspell, but not on VanDale.nl

from ..mapping import NounMap

__hard_map = NounMap({
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
    "graf": "graven" # added case for singlar
})

def pluralize_by_hard_map(singular: str, overrides: NounMap) -> str:

    for nouns in [overrides, __hard_map]:
        if nouns:
            map = nouns.get_plural_map()
            for key in map:
                if singular.endswith(key):
                    return singular[0:0-len(key)] + map[key]

    return None
    
    
def singularize_by_hard_map(plural: str, overrides: NounMap) -> str:

    for nouns in [overrides, __hard_map]:
        if nouns:
            map = nouns.get_singular_map()
            for key in map:
                if plural.endswith(key):
                    return plural[0:0-len(key)] + map[key]

    return None
