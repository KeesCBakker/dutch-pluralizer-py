
from dutch_pluralizer.mapping import NounEndingMap


def test_noun_ending_tje():

    m = NounEndingMap({
        'tje': 'tjes'
    })

    assert m.pluralize_by_endings("lepeltje") == "lepeltjes"
    assert m.singularize_by_endings("lepeltjes") == "lepeltje"



def test_noun_ending_word_replacement():

    m = NounEndingMap({
        'lasagne': 'lasagna'
    })

    assert m.pluralize_by_endings("lasagne") == "lasagna"
    assert m.singularize_by_endings("lasagna") == "lasagne"

