
from dutch_pluralizer.mapping import NounEndingMap


def test_noun_ending_map():

    m = NounEndingMap({
        'tje': 'tjes'
    })

    assert m.pluralize_by_endings("lepeltje") == "lepeltjes"
    assert m.singularize_by_endings("lepeltjes") == "lepeltje"
