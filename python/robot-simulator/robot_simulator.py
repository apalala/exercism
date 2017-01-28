from enum import IntEnum
from enum import unique


@unique
class Bearing(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


NORTH = Bearing.NORTH
EAST = Bearing.EAST
SOUTH = Bearing.SOUTH
WEST = Bearing.WEST


class Robot():
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self._coordinates = (x, y)

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def bearing(self):
        return self._bearing

    def turn_left(self):
        self._bearing = Bearing((self.bearing - 1) % len(Bearing))

    def turn_right(self):
        self._bearing = Bearing((self.bearing + 1) % len(Bearing))

    def advance(self):
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m = movement[self.bearing]
        c = self.coordinates

        self._coordinates = (c[0] + m[0], c[1] + m[1])

    def simulate(self, commands):
        action = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        for c in commands.upper():
            action[c]()
