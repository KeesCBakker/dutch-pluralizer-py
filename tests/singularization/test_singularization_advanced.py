# Tests that are not in the dictionary, but should be
# able to be solve algoritmically

from dutch_pluralizer import singularize_advanced, could_be_plural
import pytest

@pytest.mark.parametrize("plural,singular", [
    ("wenkbrauwgels", "wenkbrauwgel"),
])
def test_advanced_singular_algo(plural, singular):
    assert could_be_plural(plural) == True

    adv = singularize_advanced(plural)

    assert adv.hunspell_spelled == False

    # debug
    # print(vars(adv))
    
    assert adv.algorithic_singular[0] == singular

