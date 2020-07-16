import re
from re import Pattern
from typing import AnyStr


def create_ends_with_regex(*args: str) -> Pattern:
    s = "|".join(map(re.escape, args))
    s = f"({s})$"
    return re.compile(s)


# aas, oos, ees, uus
__r_Xs = re.compile('(aa|oo|ee|uu)s$')
__r_XXs = re.compile('(oe|eu|ui|ij|ou|au)s$')

__s_replacement_exceptions = create_ends_with_regex(
    "eis", "mens", "kans", "prins", "wens", "dans", 
    "kers", "tendens", "kaars", "fiets")

__closed_to_open = create_ends_with_regex(
    "bad", "bevel", "dag", "drag", "dak", "gebed",
    "gat", "gebrek", "glaz", "god", "grav", "hertog",
    "oorlog", "schot", "vat", "slag", "weg")

VOWELS = ['a', 'e', 'i', 'o', 'u']


def change_last_character(singular: str) -> str:

    if not singular:
        return singular

    # exclude f-plural
    if singular.endswith("f") and \
            not singular.endswith("graaf") and \
            not singular.endswith("soof") and \
            not singular.endswith("scaaf") and \
            not singular in ['cenotaaf', 'paraaf']:
        singular = singular[0:-1] + "v"

    elif __r_Xs.search(singular):
        return singular[0:-2] + "z"

    elif __r_XXs.search(singular):
        return singular[0:-1] + "z"

    elif singular.endswith("s") and \
            singular[-2] not in VOWELS and \
            not __s_replacement_exceptions.search(singular):
        singular = singular[0:-1] + "z"

    if __closed_to_open.search(singular) or len(singular) < 3:
        return singular

    if singular[-1] not in VOWELS and \
            singular[-2] in VOWELS and \
            singular[-3] not in VOWELS:
        return singular + singular[-1]

    if singular[-1] not in VOWELS and \
            singular[-2] in VOWELS and \
            singular[-3] == singular[-2]:
        return singular[0:-2] + singular[-1]

    return singular
