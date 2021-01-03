from dutch_pluralizer.strategies.helpers import create_ends_with_regex


def test_create_ends_with_regex():

    rg = create_ends_with_regex("kaas", "is", "lekker")

    assert bool(rg.search("ik heb kaas")) == True
    assert bool(rg.search("wie het is")) == True
    assert bool(rg.search("het is lekker")) == True

    assert bool(rg.search("kaas is goed")) == False
    assert bool(rg.search("is het daar")) == False
    assert bool(rg.search("lekker hoor")) == False

