from typing import Dict


def replace_by_map(mp: Dict[str, str], word: str) -> str:
    for key in mp.keys():
        if word.endswith(key):
            return word[0:0-len(key)] + mp[key]

    return None


class NounEndingMap:

    def __init__(self, map: Dict[str, str] = None):
        self.__data = {}
        self.add_range(map)


    def add(self, singular_ending: str, plural_ending: str):
        self.__data[singular_ending] = plural_ending


    def add_range(self, map: Dict[str, str]):
        if map:
            for key in map.keys():
                self.__data[key] = map[key]


    def get_plural_map(self) -> Dict[str, str]:
        return self.__data


    def get_singular_map(self) -> Dict[str, str]:
        return {v: k for k, v in self.__data.items()}


    def pluralize_by_endings(self, singular: str) -> str:
        mp = self.get_plural_map()
        return replace_by_map(mp, singular)


    def singularize_by_endings(self, plural: str) -> str:
        mp = self.get_singular_map()
        return replace_by_map(mp, plural)


