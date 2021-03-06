from dutch_pluralizer import singularize, could_be_plural
import pytest

@pytest.mark.parametrize("plural,singular", [
    ("boeken", "boek"),
    ("fietsen", "fiets"),
    ("vragen", "vraag"),
    ("ogen", "oog"),
    ("vissen", "vis"),
    ("passen", "pas"),
    ("flessen", "fles"),
    ("peren", "peer"),
    ("pollen", "pol"),
    ("polen", "pool"),
    ("agenten", "agent"),
    ("neten", "neet"),
    ("mazen", "maas"),
    ("geven", "geef"),
    ("prijzen", "prijs"),
    ("begrafenissen", "begrafenis"),
    ("beelden", "beeld"),
    ("ganzen", "gans"),
    ("kansen", "kans"),
    ("hijsen", "hijs"),
    ("ruiten", "ruit"),
    ("ambtenaren", "ambtenaar"),
    ("stukken", "stuk"),
    ("kippen", "kip"),
    ("autobiografen", "autobiograaf"),
    ("bathyscafen", "bathyscaaf"),
    ("biografen", "biograaf"),
    ("cenotafen", "cenotaaf"),
    ("choreografen", "choreograaf"),
    ("chronografen", "chronograaf"),
    ("grafen", "graaf"),
    ("kalligrafen", "kalligraaf"),
    ("oceanografen", "oceanograaf"),
    ("parafen", "paraaf"),
    ("paragrafen", "paragraaf"),
    ("stenografen", "stenograaf"),
    ("tachografen", "tachograaf"),
    ("telegrafen", "telegraaf"),
    ("theosofen", "theosoof"),
    ("fotografen", "fotograaf"),
    ("hazen", "haas"),
    ("mezen", "mees"),
    ("rozen", "roos"),
    ("infusen", "infuus"),
    ("huizen", "huis"),
    ("hoezen", "hoes"),
    ("pauzen", "paus"),
    ("octaven", "octaaf"),
    ("raven", "raaf"),
    ("varkens", "varken"),
    ("kerels", "kerel"),
    ("tafels", "tafel"),
    ("winkels", "winkel"),
    ("bezems", "bezem"),
    ("bodems", "bodem"),
    ("nozems", "nozem"),
    ("jongens", "jongen"),
    ("wagens", "wagen"),
    ("spelers", "speler"),
    ("metselaars", "metselaar"),
    ("dikkerds", "dikkerd"),
    ("grijsaards", "grijsaard"),
    ("arbeiders", "arbeider"),
    ("arbeidsters", "arbeidster"),
    ("spelers", "speler"),
    ("fietsers", "fietser"),
    ("metselaars", "metselaar"),
    ("dikkerds", "dikkerd"),
    ("arbeiders", "arbeider"),
    ("arbeidsters", "arbeidster"),
    ("meisjes", "meisje"),
    ("kopjes", "kopje"),
    ("kinderen", "kind"),
    ("eieren", "ei"),
    ("beenderen", "been"),
    ("bladeren", "blad"),
    ("kalveren", "kalf"),
    ("lammeren", "lam"),
    ("liederen", "lied"),
    ("raderen", "rad"),
    ("hoenderen", "hoen"),
    ("goederen", "goed"),
    ("gemoederen", "gemoed"),
    ("gelederen", "gelid"),
    ("etalages", "etalage"),
    ("pralines", "praline"),
    ("garages", "garage"),
    ("cafés", "café"),
    ("dominees", "dominee"),
    ("abonnees", "abonnee"),
    ("bureaus", "bureau"),
    ("diskjockeys", "diskjockey"),
    ("essays", "essay"),
    ("milieus", "milieu"),
    ("taboes", "taboe"),
    ("etuis", "etui"),
    ("auto's", "auto"),
    ("kimono's", "kimono"),
    ("ski's", "ski"),
    ("menu's", "menu"),
    ("paraplu's", "paraplu"),
    ("villa's", "villa"),
    ("firma's", "firma"),
    ("baby's", "baby"),
    ("pony's", "pony"),
    ("hobby's", "hobby"),
    ("ingenieurs", "ingenieur"),
    ("acteurs", "acteur"),
    ("generaals", "generaal"),
    ("herbergiers", "herbergier"),
    ("ooms", "oom"),
    ("tantes", "tante"),
    ("zonen", "zoon"),
    ("bruidegoms", "bruidegom"),
    ("dochters", "dochter"),
    ("scholieren", "scholier"),
    ("officieren", "officier"),
    ("sergeanten", "sergeant"),
    ("directeuren", "directeur"),
    ("premies", "premie"),
    ("revoluties", "revolutie"),
    ("directies", "directie"),
    ("knieën", "knie"),
    ("epidemieën", "epidemie"),
    ("categorieën", "categorie"),
    ("melodieën", "melodie"),
    ("industrieën", "industrie"),
    ("eisen", "eis"),
    ("mensen", "mens"),
    ("kansen", "kans"),
    ("prinsen", "prins"),
    ("kroonprinsen", "kroonprins"),
    ("wensen", "wens"),
    ("dansen", "dans"),
    ("reidansen", "reidans"),
    ("kersen", "kers"),
    ("tendensen", "tendens"),
    ("kaarsen", "kaars"),
    ("fotografen", "fotograaf"),
    ("paragrafen", "paragraaf"),
    ("filosofen", "filosoof"),
    ("ideeën", "idee"),
    ("zeeën", "zee"),
    ("feeën", "fee"),
    ("drieën", "drie"),
    ("lelies", "lelie"),
    ("baden", "bad"),
    ("bevelen", "bevel"),
    ("dagen", "dag"),
    ("vrijdagen", "vrijdag"),
    ("hoogtijdagen", "hoogtijdag"),
    ("daken", "dak"),
    ("gaten", "gat"),
    ("gebeden", "gebed"),
    ("gebreken", "gebrek"),
    ("glazen", "glas"),
    ("wijnglazen", "wijnglas"),
    ("goden", "god"),
    ("halfgoden", "halfgod"),
    ("graven", "graf"),
    ("hertogen", "hertog"),
    ("leden", "lid"),
    ("ereleden", "erelid"),
    ("oorlogen", "oorlog"),
    ("schepen", "schip"),
    ("zeeschepen", "zeeschip"),
    ("schoten", "schot"),
    ("geweerschoten", "geweerschot"),
    ("steden", "stad"),
    ("hoofdsteden", "hoofdstad"),
    ("vaten", "vat"),
    ("wijnvaten", "wijnvat"),
    ("verslagen", "verslag"),
    ("wegen", "weg"),
    ("hoofdwegen", "hoofdweg"),
    ("verdragen", "verdrag"),
    ("zeeslagen", "zeeslag"),
    ("professoren", "professor"),
    ("sectoren", "sector"),
    ("motoren", "motor"),
    ("senatoren", "senator"),
    ("processoren", "processor"),
    ("moeilijkheden", "moeilijkheid"),
    ("kleinigheden", "kleinigheid"),
    ("waarheden", "waarheid"),
    ("bezienswaardigheden", "bezienswaardigheid"),
    ("mannen", "man"),
    ("vuilnismannen", "vuilnisman"),
    ("sneeuwmannen", "sneeuwman"),
    #("veerlieden", "veerman"),
    #("handwerkslieden", "handwerksman"),
    #("bootslieden", "bootsman"),
    #("speellieden", "speelman"),
    #("Fransen", "Fransman"),
    #("Engelsen", "Engelsman"),
    ("dagjesmensen", "dagjesmens"),
    ("musea", "museum"),
    ("minima", "minimum"),
    ("maxima", "maximum"),
    ("politici", "politicus"),
    ("technici", "technicus"),
    ("musici", "musicus"),
    ("dipsauzen", "dipsaus"),
    ("catalogussen", "catalogus"),
    ("cursussen", "cursus"),
    ("albums", "album"),
    ("parfums", "parfum"),
    ("sneeën", "snee"),
    ("sneeën", "snee"),
    ("assurantiën", "assurantie"),
    ("voetencrèmes", "voetencrème"),
    ("geursamples", "geursample"),
    ("krullers", "kruller"),
    ("haarkrullers", "haarkruller"),
    ("serums", "serum"),
    ("make-ups", "make-up"),
    ("vitaminen", "vitamine"),
    ("stoffen", "stof"),
    ("vloeistoffen", "vloeistof")
])
def test_s_cases(plural, singular):
    assert could_be_plural(plural) == True
    assert singularize(plural) == singular


@pytest.mark.parametrize("singular,plural", [
    ("duw", "duwen"),
    ("schaduw", "schaduwen"),
    ("zwaluw", "zwaluwen"),
    ("leeuw", "leeuwen"),
    ("touw", "touwen"),
])
def test_s_uw(singular, plural):
    assert could_be_plural(plural) == True
    assert singularize(plural) == singular