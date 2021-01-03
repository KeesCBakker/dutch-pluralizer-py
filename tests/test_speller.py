from dutch_pluralizer.speller import new_hunspell_nl

def test_speller():

    hnspll = new_hunspell_nl()

    hnspll.add("fibulatie")
    assert hnspll.spell("fibulatie") == True

    hnspll.add("fibulaties")
    assert hnspll.spell("fibulaties") == True

    hnspll.add("argi")
    assert hnspll.spell("argi") == True

    hnspll.add("argii")
    assert hnspll.spell("argii") == True

    assert hnspll.spell("fibulatie") == True
    assert hnspll.spell("fibulaties") == True
    assert hnspll.spell("argi") == True
    assert hnspll.spell("argii") == True
