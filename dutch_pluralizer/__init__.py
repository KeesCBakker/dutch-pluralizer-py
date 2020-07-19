__version__ = "0.0.33"

__all__ = ['pluralize', 'pluralize_advanced', 'singularize',
           'could_be_plural', 'singularize_advanced', 'NounEndingMap', 'Pluralizer']

try:
    from hunspell import Hunspell
except:
    #do nothing
    a = 1


from .mapping import NounEndingMap
from .pluralizer import pluralize, pluralize_advanced
from .pluralizer_cls import Pluralizer
from .singularizer import could_be_plural, singularize, singularize_advanced
