import re

__ignored_ending = re.compile("(bevel|spel|ambtenaar)$")
__endings_with_no_preceeding_vowel = re.compile("(?<![aeiou])(el|em|en|er|aar|aard|erd)$")
__endings = re.compile("(ster|je)$")

def pluralize_with_s(singular: str) -> str:

    if __ignored_ending.search(singular):
        return None
    
    if __endings_with_no_preceeding_vowel.search(singular) or __endings.search(singular):
        return singular + "s"

    return None


def singularize_with_s(plural: str) -> str:

    if plural.endswith("s"):
        singular = plural[0:-1]
        if plural == pluralize_with_s(singular):
            return singular

    if plural.endswith("'s"):
        singular = plural[0:-2]
        if plural == pluralize_with_s(singular):
            return singular
    
    return None

    
