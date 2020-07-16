__version__ = "0.0.17"

__all__ = ['pluralize', 'pluralize_advanced', 'singularize', 'could_be_plural', 'singularize_advanced', 'NounMap']

from .pluralizer import pluralize, pluralize_advanced
from .singularizer import singularize, could_be_plural, singularize_advanced
from .mapping import NounMap