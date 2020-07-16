# numbers in this file are references to headings in this paper:
# https://sites.uclouvain.be/gramlink/Gramlink-NL/morfologie/pdf/m_nl_02_subst_03_meervoud.pdf

from dutch_pluralizer import singularize_advanced, could_be_plural
import pytest

@pytest.mark.parametrize("plural,singular", [
    ("wenkbrauwgels", "wenkbrauwgel"),
])
def test_advanced_singular_algo(plural, singular):
    assert could_be_plural(plural) == True
    adv = singularize_advanced(plural)
    print(vars(adv))
    assert adv.algorithic_singular[0] == singular

