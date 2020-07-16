__version__ = "0.0.21"

__all__ = ['pluralize', 'pluralize_advanced', 'singularize',
           'could_be_plural', 'singularize_advanced', 'NounMap', 'Pluralizer']

from hunspell import Hunspell

from .mapping import NounMap
from .pluralizer import pluralize, pluralize_advanced
from .pluralizer_cls import Pluralizer
from .singularizer import could_be_plural, singularize, singularize_advanced
