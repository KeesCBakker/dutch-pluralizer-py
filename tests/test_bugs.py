from dutch_pluralizer import singularize, pluralize
import pytest

def test_should_not_crash():
    singularize("wen")


@pytest.mark.parametrize("singular,plural", [
    ("artikel", "artikelen"),
    ("gereedschap", "gereedschappen"),
    ("middel", "middelen"),
    ("box", "boxen"),
    ("keukengerei", "keukengerei")
])
def test_random_pairs(singular, plural):
    assert pluralize(singular) == plural
    assert singularize(plural) == singular