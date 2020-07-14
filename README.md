# Dutch Noun Pluralizer in Python

Generates plural and singular nouns in a _very imperfect way_ using <a href="https://github.com/MSeal/cython_hunspell">CyHunspell</a> and OpenTaal dictionaries and <a href="https://github.com/OpenTaal/opentaal-wordlist">word lists</a>. Why imperfect? Because the Dutch language is full of exceptions.

The algorithm is based on the document <a href="https://sites.uclouvain.be/gramlink/Gramlink-NL/morfologie/pdf/m_nl_02_subst_03_meervoud.pdf">"Basismorfologie. Het meervoud in het Nederlands" (Dutch)</a> of the <a href="https://uclouvain.be/en/index.html">Université catholique de Louvain</a>.

_Note: I'm a .NET developer that does Python in my free time. I'm *&**not** a linguist, I just work for a Dutch company. Hence: this **must** be a very imperfect way of doing this._ If you have good ideas, I welcome them, just open an issue.

## Installation
Install from PIP:
```
pip install dutch-pluralizer
```

### Note on Windows 10
<a href="https://github.com/MSeal/cython_hunspell">CyHunspell</a> is used. To use this package on **Windows 10**, you might need to install <a href="https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019">Build Tools for Visual Studio 2019</a> and choose the _Windows 10 C++ SDK_ option.

## Usage - pluralization



## Development
If you want to contribute to local development, please consult <a href="">the local development page</a>.


