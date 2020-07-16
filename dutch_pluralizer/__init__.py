__version__ = "0.0.12"

__all__ = ['pluralize', 'pluralize_advanced', 'singularize', 'could_be_plural', 'singularize_advanced']

from .pluralizer import pluralize, pluralize_advanced
from .singularizer import singularize, could_be_plural, singularize_advanced