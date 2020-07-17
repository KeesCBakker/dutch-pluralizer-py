# numbers in this file are references to headings in this paper:
# https://sites.uclouvain.be/gramlink/Gramlink-NL/morfologie/pdf/m_nl_02_subst_03_meervoud.pdf

from dutch_pluralizer import pluralize
import pytest


@pytest.mark.parametrize("singular,plural", [
    ("boek", "boeken"),
    ("fiets", "fietsen"),
    ("vraag", "vragen"),
    ("oog", "ogen"),
    ("vis", "vissen"),
    ("pas", "passen"),
    ("fles", "flessen"),
    ("peer", "peren"),
    ("pol", "pollen"),
    ("pool", "polen"),
    ("agent", "agenten"),
    ("neet", "neten"),
    ("maas", "mazen"),
    ("geef", "geven"),
    ("prijs", "prijzen"),
    ("begrafenis", "begrafenissen"),
    ("beeld", "beelden"),
    ("gans", "ganzen"),
    ("kans", "kansen"),
    ("hijs", "hijsen"),
    ("ruit", "ruiten"),
    ("ambtenaar", "ambtenaren"),
    ("stuk", "stukken"),
    ("kip", "kippen")
])
def test_p_base_cases(singular, plural):
    assert pluralize(singular) == plural


# tets come from: https://onzetaal.nl/taaladvies/fotograven-fotografen/
@pytest.mark.parametrize("singular,plural", [
    ("autobiograaf", "autobiografen"),
    ("bathyscaaf", "bathyscafen"),
    ("biograaf", "biografen"),
    ("cenotaaf", "cenotafen"),
    ("choreograaf", "choreografen"),
    ("chronograaf", "chronografen"),
    ("graaf", "grafen"),
    ("kalligraaf", "kalligrafen"),
    ("oceanograaf", "oceanografen"),
    ("paraaf", "parafen"),
    ("paragraaf", "paragrafen"),
    ("stenograaf", "stenografen"),
    ("tachograaf", "tachografen"),
    ("telegraaf", "telegrafen"),
    ("theosoof", "theosofen"),
    ("fotograaf", "fotografen")
])
def test_p_f_meervoud(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("haas", "hazen"),
    ("mees", "mezen"),
    ("roos", "rozen"),
    ("infuus", "infusen"),
    ("huis", "huizen"),
    ("hoes", "hoezen"),
    ("paus", "pauzen")
])
def test_p_double_vowels(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("octaaf", "octaven"),
    ("raaf", "raven")
])
def test_p_v_mv(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("varken", "varkens"),
    ("kerel", "kerels"),
    ("tafel", "tafels"),
    ("winkel", "winkels"),
    ("bezem", "bezems"),
    ("bodem", "bodems"),
    ("nozem", "nozems"),
    ("jongen", "jongens"),
    ("wagen", "wagens"),
    ("speler", "spelers"),
    ("metselaar", "metselaars"),
    ("dikkerd", "dikkerds"),
    ("grijsaard", "grijsaards"),
    ("arbeider", "arbeiders"),
    ("arbeidster", "arbeidsters"),
    ("speler", "spelers"),
    ("fietser", "fietsers"),
    ("metselaar", "metselaars"),
    ("dikkerd", "dikkerds"),
    ("arbeider", "arbeiders"),
    ("arbeidster", "arbeidsters"),
    ("meisje", "meisjes"),
    ("kopje", "kopjes")
])
def test_p_1_2(singular, plural):
    assert pluralize(singular) == plural


# some test cases from: https://onzetaal.nl/taaladvies/eieren-eien/
@pytest.mark.parametrize("singular,plural", [
	("kind", "kinderen"),
	("ei", "eieren"),
	("been", "beenderen"),
	("blad", "bladeren"),
	("kalf", "kalveren"),
	("lam", "lammeren"),
	("lied", "liederen"),
	("rad", "raderen"),
	("hoen", "hoenderen"),
	("goed", "goederen"),
	("gemoed", "gemoederen"),
	("gelid", "gelederen")
])
def test_p_2_eren(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
	("etalage", "etalages"),
	("praline", "pralines"),
	("garage", "garages"),
	("café", "cafés"),
	("dominee", "dominees"),
	("abonnee", "abonnees"),
	("bureau", "bureaus"),
	("diskjockey", "diskjockeys"),
	("essay", "essays"),
	("milieu", "milieus"),
	("taboe", "taboes"),
	("etui", "etuis"),
    #("emoji", "emoji's"),
    ("scampi", "scampi's"),
    #("blini", "blini's"),
    #("lasagne", "lasagna"),
])
def test_p_3_bastard_words(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("auto", "auto's"),
	("kimono", "kimono's"),
	("ski", "ski's"),
	("menu", "menu's"),
	("paraplu", "paraplu's"),
	("villa", "villa's"),
	("firma", "firma's"),
	("baby", "baby's"),
	("pony", "pony's"),
	("hobby", "hobby's"),
    ("euro", "euro's"),
    #("soa", "soa's"),
    #("cfk", "cfk's"),
])
def test_p_4_long_ending(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("ingenieur", "ingenieurs"),
    ("acteur", "acteurs"),
    ("generaal", "generaals"),
    ("herbergier", "herbergiers"),
    ("oom", "ooms"),
    ("tante", "tantes"),
    ("zoon", "zonen"),
    ("bruidegom", "bruidegoms"),
    ("dochter", "dochters"),
    ("scholier", "scholieren"),
    ("officier", "officieren"),
    ("sergeant", "sergeanten"),
    ("directeur", "directeuren"),
    ("directrice", "directrices")
])
def test_p_5_family_and_occupations(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("premie", "premies"),
    ("revolutie", "revoluties"),
    ("directie", "directies")
])  
def test_p_6_1_ie(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("knie", "knieën"),
    ("epidemie", "epidemieën"),
    ("categorie", "categorieën"),
    ("melodie", "melodieën"),
    ("industrie", "industrieën"),
])  
def test_p_6_2_ie(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("eis", "eisen"),
    ("mens", "mensen"),
    ("kans", "kansen"),
    ("prins", "prinsen"),
    ("kroonprins", "kroonprinsen"),
    ("wens", "wensen"),
    ("dans", "dansen"),
    ("reidans", "reidansen"),
    ("kers", "kersen"),
    ("tendens", "tendensen"),
    ("kaars", "kaarsen"),
    ("fotograaf", "fotografen"),
    ("paragraaf", "paragrafen"),
    ("filosoof", "filosofen"),
])  
def test_p_9_1(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("idee", "ideeën"),
    ("zee", "zeeën"),
    ("fee", "feeën"),
    ("drie", "drieën"),
    ("lelie", "lelies"),
])
def test_p_9_2_trema(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("bad", "baden"),
    ("bevel", "bevelen"),
    ("dag", "dagen"),
    ("vrijdag", "vrijdagen"),
    ("hoogtijdag", "hoogtijdagen"),
    ("dak", "daken"),
    ("gat", "gaten"),
    ("gebed", "gebeden"),
    ("gebrek", "gebreken"),
    ("glas", "glazen"),
    ("wijnglas", "wijnglazen"),
    ("god", "goden"),
    ("halfgod", "halfgoden"),
    ("graf", "graven"),
    ("hertog", "hertogen"),
    ("lid", "leden"),
    ("erelid", "ereleden"),
    ("oorlog", "oorlogen"),
    ("schip", "schepen"),
    ("zeeschip", "zeeschepen"),
    ("schot", "schoten"),
    ("geweerschot", "geweerschoten"),
    ("stad", "steden"),
    ("hoofdstad", "hoofdsteden"),
    ("vat", "vaten"),
    ("wijnvat", "wijnvaten"),
    ("verslag", "verslagen"),
    ("weg", "wegen"),
    ("hoofdweg", "hoofdwegen"),
    ("verdrag", "verdragen"),
    ("zeeslag", "zeeslagen"),
    ("smid", "smeden"),
    ("zilversmid", "zilversmeden")
])
def test_p_9_3(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("professor", "professoren"),
    ("sector", "sectoren"),
    ("motor", "motoren"),
    ("senator", "senatoren"),
    ("processor", "processoren"),
])
def test_p_9_4(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("moeilijkheid", "moeilijkheden"),
    ("kleinigheid", "kleinigheden"),
    ("waarheid", "waarheden"),
    ("bezienswaardigheid", "bezienswaardigheden"),
])
def test_p_9_5(singular, plural):
    assert pluralize(singular) == plural


# more info at: https://onzetaal.nl/taaladvies/tuinmannen-tuinlieden-of-tuinlui/
@pytest.mark.parametrize("singular,plural", [
    ("man", "mannen"),
    ("vuilnisman", "vuilnismannen"),
    ("sneeuwman", "sneeuwmannen"),
    ("veerman", "veerlieden"),
    ("handwerksman", "handwerkslieden"),
    ("bootsman", "bootslieden"),
    ("speelman", "speellieden"),
    ("Fransman", "Fransen"),
    ("Engelsman", "Engelsen"),
    ("dagjesmens", "dagjesmensen"),
])
def test_p_9_6(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("museum", "musea"),
    ("minimum", "minima"),
    ("maximum", "maxima"),
    ("politicus", "politici"),
    ("technicus", "technici"),
    ("musicus", "musici"),
    ("dipsaus", "dipsauzen"),
    ("catalogus", "catalogussen"),
    ("cursus", "cursussen"),
    ("curriculum", "curricula")
])
def test_p_9_7(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("album", "albums"),
    ("parfum", "parfums"),
])
def test_p_9_7_exceptions(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("duw", "duwen"),
    ("schaduw", "schaduwen"),
    ("zwaluw", "zwaluwen"),
    ("leeuw", "leeuwen"),
    ("touw", "touwen"),
])
def test_p_uw(singular, plural):
    assert pluralize(singular) == plural


@pytest.mark.parametrize("singular,plural", [
    ("snee", "sneeën"),
    ("snee", "sneeën"),
    ("assurantie", "assurantiën"),
    ("voetencrème", "voetencrèmes"),
    ("geursample", "geursamples"),
    ("kruller", "krullers"),
    ("haarkruller", "haarkrullers"),
    ("serum", "serums"),
    ("make-up", "make-ups"),
    ("bh", "bh's"),
    ("up", "ups"),
    ("vitamine", "vitamines"),
    ("stof", "stoffen"),
    ("vloeistof", "vloeistoffen"),
    ("lenzenvloeistof", "lenzenvloeistoffen"),
    ("gluut", "gluten"),
    ("logé", "logés"),
    ("logee", "logees"),
    ("stagiair", "stagiairs"),
    ("stagiaire", "stagiaires")
])
def test_p_general_cases(singular, plural):
    assert pluralize(singular) == plural




