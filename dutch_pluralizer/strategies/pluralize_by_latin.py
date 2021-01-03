import re

from .helpers import create_ends_with_regex

__sen_endings = create_ends_with_regex('catalogus')

def pluralize_by_latin(singular: str) -> str:
    if singular.endswith("aus"):
        return None
    if singular.endswith("um"):
        return singular[0:-2] + "a"
    if __sen_endings.search(singular):
        return singular + "sen"
    if singular.endswith("cus"):
        return singular[0:-3] + "ci"
    if singular.endswith("us"):
        return singular[0:-2] + "i"
    return None


def singularize_by_latin(plural: str) -> str:
    
    if plural.endswith("a"):
        return plural[0:-1] + "um"

    if plural.endswith("ci"):
        return plural[0:-2] + "cus"

    if plural.endswith("i"):
        return plural[0:-1] + "us"

    return None
