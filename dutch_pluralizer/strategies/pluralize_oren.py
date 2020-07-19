# pluralizers that are not so complex, they have an ending and no exceptions

import re

__r_or = re.compile("[^o]or$")
__r_oren = re.compile("[^o]oren$")


def pluralize_oren(singular: str) -> str:

    if __r_or.search(singular):
        return singular + "en"

    return None


def singularize_oren(plural: str) -> str:

    if __r_oren.search(plural):
        return plural[0:-2]

    return None
