"""
Base class that realizes trees in the forest.
"""


class Tree:
    def __init__(self,
                 name: str = "Tree",
                 coord_x: int = 0,
                 coord_y: int = 0,
                 ):
        self._name: str = name
        self._coord_x: int = coord_x
        self._coord_y: int = coord_y

    def clone(self):
        return Tree(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def coord_x(self):
        return self._coord_x

    @coord_x.setter
    def coord_x(self, coord_x: str):
        self._coord_x = coord_x

    @property
    def coord_y(self):
        return self._coord_y

    @coord_y.setter
    def coord_y(self, coord_y: str):
        self._coord_y = coord_y

    def __str__(self):
        return (f"Name: {self._name} \n"
                f"coord: ({self._coord_x, self._coord_y}) \n")
