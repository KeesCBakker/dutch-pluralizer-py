__lui_endings = []
__lieden_endings = ['veer', 'handwerks', 'boots', 'boots', 'speel']
__en_endings = ["Frans", "Engels", "frans", "engels", "mens"]

def pluralize_man(singlar: str) -> str:
    if not singlar.endswith("man"):
        return None

    root = singlar[0:-3]

    if root in __lui_endings:
        return root + "lui"

    if root in __lieden_endings:
        return root + "lieden"

    if root in __en_endings:
        return root + "en"

    return None