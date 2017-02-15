

EARTH_ORBITAL_SECONDS = 31557600

PLANET_YEAR_RATIO = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}


class SpaceAge():
    def __init__(self, age):
        self.seconds = age

    def _on_earth_years(self):
        return self.seconds / EARTH_ORBITAL_SECONDS

    @classmethod
    def __static_init__(cls):
        def make_method(ratio):
            return lambda self: round(self._on_earth_years() / ratio, 2)

        for planet, ratio in PLANET_YEAR_RATIO.items():
            setattr(cls, 'on_%s' % planet.lower(), make_method(ratio))

    def __getattr__(self, item):
        if item.startswith('on_') and item[3:] in PLANET_YEAR_RATIO:
            self.__static_init__()
        return super().__getattribute__(item)
