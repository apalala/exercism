

_ALLERGENS = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats',
]
_ALLERGEN_VALUE = {a: 2**i for i, a in enumerate(_ALLERGENS)}

class Allergies():
    def __init__(self, score):
        self.score = score

    @property
    def lst(self):
        return [
            allergen
            for allergen in _ALLERGENS
            if _ALLERGEN_VALUE[allergen] & self.score
        ]

    def is_allergic_to(self, allergen):
        return _ALLERGEN_VALUE[allergen] & self.score
