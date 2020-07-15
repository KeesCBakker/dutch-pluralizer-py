# Dutch Noun Pluralizer in Python

Generates plural and singular nouns in a _very imperfect way_ using <a href="https://github.com/MSeal/cython_hunspell">CyHunspell</a> and OpenTaal dictionaries and <a href="https://github.com/OpenTaal/opentaal-wordlist">word lists</a>. Why imperfect? Because the Dutch language is full of exceptions.

The algorithm is based on the document <a href="https://sites.uclouvain.be/gramlink/Gramlink-NL/morfologie/pdf/m_nl_02_subst_03_meervoud.pdf">"Basismorfologie. Het meervoud in het Nederlands" (Dutch)</a> of the <a href="https://uclouvain.be/en/index.html">Université catholique de Louvain</a>.

_Note: I'm a .NET developer that does Python in my free time. I'm **not** a linguist, I just work for a Dutch company. Hence: this **must** be a very imperfect way of doing this._ If you have good ideas, I welcome them, just open an issue.

## Installation
Install from PIP:
```
pip install dutch-pluralizer
```

**Note on Windows 10**
<a href="https://github.com/MSeal/cython_hunspell">CyHunspell</a> is used. To use this package on **Windows 10**, you might need to install <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019">Build Tools for Visual Studio 2019</a> and choose the _Windows 10 C++ SDK_ option.

## CLI usage
The project can be used as a CLI tool:
```
usage: __main__.py [-h] [-p] [-s] [-pa] [-v] word

Generates Dutch plural and singular nouns in a very imperfect way using Hunspell     
dictionaries. Why imperfect? Because the Dutch language is full of exceptions.       

positional arguments:
  word                  The word.

optional arguments:
  -h, --help            show this help message and exit
  -p, --pluralize       pluralizes the word.
  -s, --singularize     singularizes the word.
  -pa, --pluralize_advanced
                        shows advanced pluralization output.
  -v, --verbose         Shows an error message when a word could not be processed.   
```

### API
The API can be used like this:

```python
from dutch_pluralizer import pluralize, singularize

# pluralize will return the result or None
assert pluralize("kaas") == "kazen"
assert pluralize("kazen") == None

# singularize will return the result or None
assert singularize("kazen") == "kaas"
assert singularize("kaas") == None
```

Advanced pluralization will give you more options:

```python
from dutch_pluralizer import pluralize, pluralize_advanced, singularize

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

```

Add custom words to the dictionary:

```python
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
```


## Help!? The result is not correct
I told you it was imperfect! There is stuff this package can and cannot do:

- We cannot discover words that are not recognized by Hunspell
- We can only process **nouns** (Dutch: zelfstandige naamwoorden)
- We can only return a single result, but we know that the singular of _graven_ can be either _graaf_ or _graf_. We currently have no support for these use cases.
- We can add words, just open up a ticket on <a href="https://github.com/keescbakker/dutch-pluralizer-py/issues">GitHub</a>. Please make sure you provide some evidence on why the word should be added (like a VanDale.nl result).


## Development
If you want to contribute to local development, please consult <a href="https://github.com/KeesCBakker/dutch-pluralizer-py/blob/master/DEV.md">the local development page</a>.


