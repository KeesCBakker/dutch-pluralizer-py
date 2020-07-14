# Yeah, sometimes is is too hard to do it algoritmically, or I'm
# just way too lazy, so here is a map for all those silly exceptions
# that we like to have in Dutch.
# Other words that end up here have plurals that are excepted by
# Hunspell, but not on VanDale.nl

__hard_map = {
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
}

__inversed_hard_map = {v: k for k, v in __hard_map.items()}

def pluralize_by_hard_map(singular: str) -> str:
    for key in __hard_map:
        if singular.endswith(key):
            return singular[0:0-len(key)] + __hard_map[key]

    return None


def singularize_by_hard_map(plural: str) -> str:
    for key in __inversed_hard_map:
        if plural.endswith(key):
            return plural[0:0-len(key)] + __inversed_hard_map[key]

    return None
