from dutch_pluralizer import pluralize_advanced
from pprint import pprint

import pytest
import json


def test_p_hijsen():
    result = pluralize_advanced("hijs")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.switched_ending_from == "zen"
    assert result.switched_ending_to == "sen"


def test_p_snede():
    result = pluralize_advanced("snede")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.switched_ending_from == "des"
    assert result.switched_ending_to == "den"


def test_p_drie():
    result = pluralize_advanced("drie")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.switched_ending_from == "iën"
    assert result.switched_ending_to == "ieën"


def test_p_album():
    result = pluralize_advanced("album")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.switched_ending_from == "a"
    assert result.switched_ending_to == "ums"


def test_p_cursus():
    result = pluralize_advanced("cursus")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.switched_ending_from == "i"
    assert result.switched_ending_to == "ussen"


def test_p_oogpotlood():
    result = pluralize_advanced("oogpotlood")
    assert result.algorithmic_plural != result.plural
    assert result.algorithmic_plural == "oogpotloden"


def test_p_wenkbrauwgel():

    result = pluralize_advanced("wenkbrauwgel")
    #pprint(vars(result))
    assert result.algorithmic_plural != result.plural
    assert result.algorithmic_plural == "wenkbrauwgels"

def pluralize_advanced_algo_result(str: str) -> str:
    return pluralize_advanced(str).algorithmic_plural


@pytest.mark.parametrize("singular,plural", [
    ("auto", "auto's"),
    ("kimono", "kimono's"),
    ("ski", "ski's"),
    ("menu", "menu's"),
    ("paraplu", "paraplu's"),
    ("firma", "firma's"),
    ("baby", "baby's"),
    ("pony", "pony's"),
    ("hobby", "hobby's"),
    ("diskjockey", "diskjockeys"),
    ("essay", "essays")
])
def test_p_4_adv_long_ending(singular, plural):
    assert pluralize_advanced_algo_result(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("astrosoof", "astrosofen"),
    ("digraaf", "digrafen"),
    ("fonetograaf", "fonetografen"),
    ("fonosoof", "fonosofen"),
    ("mesoscaaf", "mesoscafen"),
    ("tomograaf", "tomografen"),
    ("xenograaf", "xenografen"),
    ("xylograaf", "xylografen"),
])
def test_p_adv_f_mv(singular, plural):
    # tests come from: https://onzetaal.nl/taaladvies/fotograven-fotografen/
    assert pluralize_advanced_algo_result(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("bh", "bh's"),
    ("voedingsbh", "voedingsbh's"),
    ("chino", "chino's"),
])
def test_p_adv_general(singular, plural):
    assert pluralize_advanced_algo_result(singular) == plural
