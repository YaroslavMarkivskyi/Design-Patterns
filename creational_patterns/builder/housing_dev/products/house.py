"""
Class that describes house.
It can be:

"""
from typing import List, Any


class House:
    def __init__(self) -> None:
        self._parts: List = []

    def add(self, part: Any) -> None:
        self._parts.append(part)

    def list_parts(self) -> List:
        return self._parts

    def __str__(self):
        return f"Product parts:\n {'\n '.join(self._parts)}"
