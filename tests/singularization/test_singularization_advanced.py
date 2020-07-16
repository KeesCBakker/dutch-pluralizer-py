# Tests that are not in the dictionary, but should be
# able to be solve algoritmically

from dutch_pluralizer import NounMap, could_be_plural, singularize_advanced
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



@pytest.mark.parametrize("plural,singular", [
    ("mode", "mode"),
    ("beenmode", "beenmode"),
    ("kleding", "kleding"),
    ("badkleding", "badkleding"),
])
def test_advanced_singluar_override_endings(plural, singular):

    overrides = NounMap({plural: singular})

    assert could_be_plural(plural, ending_overrides=overrides) == True

    adv = singularize_advanced(plural, ending_overrides=overrides)

    # debug
    #print(vars(adv))
    
    assert adv.algorithic_singular[0] == singular


