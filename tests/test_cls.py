import pytest
from dutch_pluralizer import Pluralizer, NounEndingMap
from dutch_pluralizer.speller import new_hunspell_nl

@pytest.mark.parametrize("singular,plural", [
    ("serum", "serums"),
    ("argi", "argii"),
    ("fibulatie", "fibulaties")
])
def test_pluralizer_scenarios(singular, plural):
    
    overrides = NounEndingMap({"argi": "argii"})
    hnspll = new_hunspell_nl()
    hnspll.add("fibulatie")
    hnspll.add("argi")
    hnspll.add("argii")
    hnspll.add("fibulaties")

    p = Pluralizer(hnspll, overrides)

    assert p.pluralize_advanced(singular).plural == plural
    assert p.singularize_advanced(plural).singular == singular