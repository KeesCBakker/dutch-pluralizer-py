from dutch_pluralizer import singularize
import pytest

def test_should_not_crash():
    singularize("wen")