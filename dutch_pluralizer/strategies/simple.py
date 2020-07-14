# pluralizers that are not so complex, they have an ending and no exceptions

def pluralize_oren(singular: str)-> str:
    if not singular.endswith("or"):
        return None
    
    return singular + "en"


def singularize_oren(plural:str)->str:

    # make sure we don't get too many false positive
    if not plural.endswith("oren") or len(plural) < 8:
        return None

    return plural[0:-2]


def pluralize_heid(singular: str) -> str:
    if not singular.endswith("heid"):
        return None
    
    return singular[0:-2] + "den"


def singularize_heid(plural: str) -> str:
    if not plural.endswith("heden"):
        return None
    
    return plural[0:-5] + "heid"


def pluralize_lui(singular: str) -> str:
    if not singular.endswith("lui"):
        return None
    
    return singular[0:-2] + "ieden"


def pluralize_lui(singular: str) -> str:
    if not singular.endswith("lui"):
        return None

    return singular[0:-2] + "ieden"


def singularize_jes(plural: str) -> str:

    if not plural.endswith("jes"):
        return None

    return plural[0:-1]