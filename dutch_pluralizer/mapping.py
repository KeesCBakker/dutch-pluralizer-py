from typing import Dict

class NounMap:

    def __init__(self, dict: Dict[str, str] = None):
        self.__data = {}
        if dict:
            self.add_range(dict)

    def add(self, singular_ending: str, plural_ending: str):
        self.__data[singular_ending] = plural_ending

    def add_range(self, dict: Dict[str, str]):
        for key in dict.keys():
            self.__data[key] = dict[key]

    def get_plural_map(self) -> Dict[str, str]:
        return self.__data

    def get_singular_map(self) -> Dict[str, str]:
        return {v: k for k, v in self.__data.items()}
