from hunspell import Hunspell

from .mapping import NounEndingMap
from .pluralizer import (AdvancedPluralizationResult, pluralize,
                         pluralize_advanced)
from .singularizer import (AdvancedSingularizationResult, could_be_plural,
                           singularize, singularize_advanced)
from .speller import ensure_hunspell_nl


class Pluralizer:

    def __init__(self, speller: Hunspell = None, ending_overrides: NounEndingMap = None):
        super().__init__()

        self.__speller = speller or ensure_hunspell_nl()
        self.__ending_overrides = ending_overrides


    def add_ending_overrides(self, ending_overrides: NounEndingMap):

        if ending_overrides:
            if(self.__ending_overrides == None):
                self.__ending_overrides = NounEndingMap()

            self.__ending_overrides.add_range(
                ending_overrides.get_plural_map())


    def singularize(self, plural: str) -> str:
        return singularize(plural, self.__speller, self.__ending_overrides)


    def singularize_advanced(self, plural: str) -> AdvancedSingularizationResult:
        return singularize_advanced(plural, self.__speller, self.__ending_overrides)


    def could_be_plural(self, plural: str) -> bool:
        return could_be_plural(plural, self.__ending_overrides)


    def pluralize(self, singular: str) -> str:
        return pluralize(singular, self.__speller, self.__ending_overrides)


    def pluralize_advanced(self, singular: str) -> AdvancedPluralizationResult:
        return pluralize_advanced(singular, self.__speller, self.__ending_overrides)
