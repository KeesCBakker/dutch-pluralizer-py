import re

from .helpers import change_last_character

__long_vowel_endings_with_no_preceeding_vowel = re.compile("(?<![aeiou])(a|o|u|i|y)$")

def pluralize_long_vowel(singular: str) -> str:
    
    if __long_vowel_endings_with_no_preceeding_vowel.search(singular):
        return singular + "'s"

    return None
