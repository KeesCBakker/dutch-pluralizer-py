import re

from .helpers import VOWELS

__r_bastard_endings = re.compile("(é|eau|ey|ay|ieu|oe|ui)$")

def pluralize_bastard(singular: str) -> str:

    # dominee, abonnee
    if singular.endswith("nee") and not singular.endswith("snee"):
        return singular + "s"

    if singular.endswith("e") and singular[-2] not in VOWELS:
        return singular + "s"

    if __r_bastard_endings.search(singular):
        return singular + "s"

    return None
