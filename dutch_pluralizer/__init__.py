__version__ = "0.0.11"

__all__ = ['pluralize', 'pluralize_advanced', 'singularize', 'could_be_plural']

from .pluralizer import pluralize, pluralize_advanced
from .singularizer import singularize, could_be_plural