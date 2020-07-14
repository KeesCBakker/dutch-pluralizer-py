import re

from .helpers import VOWELS, change_last_character, create_ends_with_regex

__eren_endings = create_ends_with_regex("kind", "ei", "been", "blad", "kalf", "lam", "lied", "rund", "goed", "gemoed", "hoen", "rad", "gelid")
__deren_endings = create_ends_with_regex("been", "hoen")
__excetions_last_character_changed = create_ends_with_regex('blad', 'lied', 'rad', 'goed', 'gemoed')


def pluralize_eren(singular: str) -> str:

    if not __eren_endings.search(singular):
        return None

    if __deren_endings.search(singular):
        singular += 'd'

    if not __excetions_last_character_changed.search(singular):
        singular = change_last_character(singular)

    return singular + 'eren'


def singularize_eren(plural: str) -> str:

    if len(plural) < 6:
        return None

    if plural.endswith("eren"):
        singular = plural[0:-4]

        if singular.endswith("d"):
            minus_d = singular[0:-1]
            if __deren_endings.search(minus_d):
                return minus_d

        if singular.endswith("v"):
            return singular[0:-1] + "f"

        if singular[-1] not in VOWELS and \
            singular[-1] == singular[-2]:
            return singular[0:-1]

        return singular


    return None
