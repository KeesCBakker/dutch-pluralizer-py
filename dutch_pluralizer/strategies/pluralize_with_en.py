from .helpers import change_last_character, create_ends_with_regex, VOWELS
import re

def pluralize_with_en(singular: str) -> str:
    singular = change_last_character(singular)

    if singular.endswith("ie"):
        return singular[0:-1] + "ën"
    
    if singular.endswith("e"):
        return singular + "ën"

    return singular + "en"


__xxx = re.compile("(^|[^aeoiu])[aeoiu][^aeoiu]$")


def singularize_with_trema_en(plural: str)->str:

    if plural.endswith("iën"):
        return plural[0:-2] + "e"

    if plural.endswith("ën"):
        return plural[0:-2]

    return None


__aaa = create_ends_with_regex("weg", "vat", "schot", "gat", "drag", "bad", "dag", "bevel")

def singularize_with_en_single_vowel(plural: str) -> str:

    if not plural.endswith("en"):
        return None

    singular = plural[0:-2]
    if not __aaa.search(singular):
        return None

    if singular.endswith("v"):
        return singular[0:-1] + "f"

    if singular.endswith("z"):
        return singular[0:-1] + "s"

    return singular


def singularize_with_en_double_vowel(plural: str) -> str:

    if not plural.endswith("en"):
        return None

    # ogen => oog
    singular = plural[0:-2]
    if __xxx.search(singular):
        singular = singular[0:-1] + singular[-2] + singular[-1]

        if singular.endswith("v"):
            return singular[0:-1] + "f"
        if singular.endswith("z"):
            return singular[0:-1] + "s"

        return singular


    return None

def singularize_with_en_double_consonant(plural: str) -> str:

    if not plural.endswith("en"):
        return None

    singular = plural[0:-2]
    if singular[-1] not in VOWELS and \
        singular[-1] == singular[-2] and \
        singular[-3] in VOWELS:
        return singular[0:-1]

    return None