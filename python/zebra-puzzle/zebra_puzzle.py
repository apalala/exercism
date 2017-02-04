# from the solution by @BrianLusina
# http://exercism.io/submissions/a824ec60503e469db9e126a83f5e3cfa

from collections import namedtuple
from itertools import permutations


Color = namedtuple('Color', 'red green ivory yellow blue')
Person = namedtuple('Person', 'englishman spaniard ukranian japanese norwegian')
Drink = namedtuple('Drinks', 'coffee tea milk orange_juice, water')
Smokes = namedtuple('Smokes', 'old_gold kools chesterfields lucky_strike parliaments')
Pet = namedtuple('Pet', 'dog snails fox horse zebra')
Houses = namedtuple('Houses', 'color person drink smokes pet')


def solution():
    result = _find_solutions()[0]
    persons = {
        value: name.capitalize()
        for name, value in result.person._asdict().items()}
    return (
        "It is the {} who drinks the water.\n"
        "The {} keeps the zebra."
    ).format(
        persons[result.drink.water],
        persons[result.pet.zebra]
    )


def _find_solutions():
    def is_same_house(x, y):
        return x == y

    def is_right_of(x, y):
        return x - y == 1

    def is_next_to(x, y):
        return abs(x - y) == 1

    house_numbers = range(5)
    first, second, middle, third, last = house_numbers

    orderings = list(permutations(house_numbers))
    return [
        Houses(color=color, person=person, drink=drink, smokes=smokes, pet=pet)
        for color in (Color(*c) for c in orderings)
        if (
            is_right_of(color.green, color.ivory)
        )
        for person in (Person(*w) for w in orderings)
        if (
            is_same_house(person.englishman, color.red) and
            is_same_house(person.norwegian, first) and
            is_next_to(person.norwegian, color.blue)
        )
        for drink in (Drink(*d) for d in orderings)
        if (
            is_same_house(drink.coffee, color.green) and
            is_same_house(person.ukranian, drink.tea) and
            is_same_house(drink.milk, middle)
        )
        for smokes in (Smokes(*s) for s in orderings)
        if (
            is_same_house(smokes.kools, color.yellow) and
            is_same_house(smokes.lucky_strike, drink.orange_juice) and
            is_same_house(person.japanese, smokes.parliaments)
        )
        for pet in (Pet(*p) for p in orderings)
        if (
            is_same_house(person.spaniard, pet.dog) and
            is_same_house(smokes.old_gold, pet.snails) and
            is_next_to(smokes.chesterfields, pet.fox) and
            is_next_to(smokes.kools, pet.horse)
        )
    ]
