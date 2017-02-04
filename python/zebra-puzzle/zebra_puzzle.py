# from the solution by @BrianLusina
# http://exercism.io/submissions/a824ec60503e469db9e126a83f5e3cfa

from collections import namedtuple
from itertools import permutations


Color = namedtuple('Color', 'red green ivory yellow blue')
Who = namedtuple('Who', 'englishman spaniard ukranian japanese norwegian')
Drink = namedtuple('Drinks', 'coffee tea milk orange_juice, water')
Smokes = namedtuple('Smokes', 'old_gold kools chesterfields lucky_strike parliaments')
Pet = namedtuple('Pet', 'dog snails fox horse zebra')


def solution():
    houses = range(5)
    first, second, middle, third, last = houses

    orderings = list(tuple(p) for p in permutations(houses))
    result = [
        (color, who, drink, smokes, pet)
        for color in (Color(*c) for c in orderings)
        if (
            _right_of(color.green, color.ivory)
        )
        for who in (Who(*w) for w in orderings)
        if (
            who.englishman == color.red and
            who.norwegian == first and
            _next_to(who.norwegian, color.blue)
        )
        for drink in (Drink(*d) for d in orderings)
        if (
            drink.coffee == color.green and
            who.ukranian == drink.tea and
            drink.milk == middle
        )
        for smokes in (Smokes(*s) for s in orderings)
        if (
            smokes.kools == color.yellow and
            smokes.lucky_strike == drink.orange_juice and
            who.japanese == smokes.parliaments
        )
        for pet in (Pet(*p) for p in orderings)
        if (
            who.spaniard == pet.dog and
            smokes.old_gold == pet.snails and
            _next_to(smokes.chesterfields, pet.fox) and
            _next_to(smokes.kools, pet.horse)
        )
    ]
    color, who, drink, smokes, pet = result[0]

    who_names = {value: name.capitalize() for name, value in who._asdict().items()}
    return (
        "It is the {} who drinks the water.\n"
        "The {} keeps the zebra."
    ).format(who_names[drink.water], who_names[pet.zebra])


def _right_of(x, y):
    return x - y == 1


def _next_to(x, y):
    return abs(x - y) == 1
