from dutch_pluralizer import pluralize, pluralize_advanced, singularize
from hunspell import Hunspell

def test_readme_example_1():

    # pluralize will return the result or None
    assert pluralize("kaas") == "kazen"
    assert pluralize("kazen") == None

    # singularize will return the result or None
    assert singularize("kazen") == "kaas"
    assert singularize("kaas") == None


def test_readme_example_2():

    adv = pluralize_advanced("album")

    # the plural
    assert adv.plural == 'albums'

    # what the algorithm (without Hunspell) created
    # is probably not correct, that's why Hunspell is
    # used on it. It is like a preprocessing:
    assert adv.algorithmic_plural == 'alba'

    # indicates that end result was found in Hunspell
    adv.hunspell_spelled = True

    # the plural was found by replacement of 
    # 'a' to 'ums'
    assert adv.switched_ending_from == 'a'
    assert adv.switched_ending_to == 'ums'

    # suggestions given by Hunspell when the algorithmic
    # result was processed:
    assert adv.suggestions == ( 'Alba',
                                'aba',        
                                'balba',
                                'albe',
                                'alia',
                                'alla',
                                'alma',
                                'alfa',
                                'Elba')


from dutch_pluralizer import pluralize, singularize
from dutch_pluralizer.speller import ensure_hunspell_nl

def test_readme_example_3():

    # default dictionary does not understand these words,
    # as they are not Dutch
    assert pluralize("fibulatie") == None
    assert singularize("fibulaties") == None

    # add the words to the dictionary
    h = ensure_hunspell_nl()
    h.add("fibulatie")
    h.add("fibulaties")

    # check again
    assert pluralize("fibulatie", speller=h) == "fibulaties"
    assert singularize("fibulaties", speller=h) == "fibulatie"


