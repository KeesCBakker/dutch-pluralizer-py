from dutch_pluralizer import pluralize, pluralize_advanced, singularize

def test_readme_example():

    # pluralize will return the result or None
    assert pluralize("kaas") == "kazen"
    assert pluralize("kazen") == None

    # singularize will return the result or None
    assert singularize("kazen") == "kaas"
    assert singularize("kaas") == None

    # advanced pluralization will give you more
    # output:
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