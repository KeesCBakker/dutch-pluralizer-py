from typing import Dict

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
