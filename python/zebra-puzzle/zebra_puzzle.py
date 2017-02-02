from enum import Enum
from itertools import count

class R(Enum):
    NUMBER = 0
    NEXT = 1
    WHO = 2
    COLOR = 3
    OWNS = 4
    DRINKS = 5
    SMOKES = 6


def _error(a, b):
    raise ValueError('Cannot unify %s with %s' % (a, b))


class Var():
    counter = count()
    def __init__(self):
        self._id = next(self.counter)
        self._value = None

    def value(self):
        if self._value is None:
            return None
        elif isinstance(self._value, Var):
            return self._value.value()
        else:
            return self._value

    def set(self, value):
        if self._value is None:
            print(self)
            self._value = value
        elif isinstance(self._value, Var):
            self._value.set(value)
        else:
            _error(self, value)

    def unify(self, other):
        if self == other:
            pass
        elif self.value() is None:
            self.set(other)
        elif isinstance(other, Var):
            other.set(self)
        else:
            _error(self, other)

    def __repr__(self):
        return '%d: %s' % (self._id, str(self._value))


def var():
    return Var()


def unify(a, b):
    if isinstance(a, Var):
        a.unify(b)
    elif isinstance(b, Var):
        b.unify(a)
    elif isinstance(a, tuple) and isinstance(b, tuple) and a[1] == b[1]:
        for x, y in zip(a, b):
            unify(x, y)
        print(a, b)
    elif a != b:
        _error(a, b)


def facts():
    # 1
    f = []
    f += [
        (0, R.NUMBER, 0),
        (1, R.NUMBER, 1),
        (2, R.NUMBER, 2),
        (3, R.NUMBER, 3),
        (4, R.NUMBER, 4),
        (1, R.NEXT, 0),
        (2, R.NEXT, 1),
        (3, R.NEXT, 2),
        (4, R.NEXT, 3),
    ]
    # 2
    h = var()
    f += [
        (h, R.WHO, 'Englishman'),
        (h, R.COLOR, 'red'),
    ]
    # 3
    h = var()
    f += [
        (h, R.WHO, 'Spaniard'),
        (h, R.OWNS, 'dog'),
    ]
    # 4
    h = var()
    f += [
        (h, R.DRINKS, 'coffee'),
        (h, R.COLOR, 'green'),
    ]
    # 5
    h = var()
    f += [
        (h, R.WHO, 'Ukranian'),
        (h, R.DRINKS, 'tea'),
    ]
    # 6
    h1 = var()
    h2 = var()
    f += [
        (h1, R.COLOR, 'green'),
        (h2, R.COLOR, 'ivory'),
        (h1, R.NEXT, h2),
    ]
    # 7
    h = var()
    f += [
        (h, R.SMOKES, 'Old Gold'),
        (h, R.OWNS, 'snails'),
    ]
    # 8
    h = var()
    f += [
        (h, R.COLOR, 'yellow'),
        (h, R.SMOKES, 'Kools'),
    ]
    # 9
    h = var()
    f += [
        (2, R.DRINKS, 'milk'),
    ]
    # 10
    h = var()
    f += [
        (0, R.WHO, 'Norweigan'),
    ]
    # 11
    h1 = var()
    h2 = var()
    f += [
        (h1, R.SMOKES, 'Chesterfields'),
        (h2, R.OWNS, 'fox'),
        (h1, R.NEXT, h2)
    ]
    # 12
    h1 = var()
    h2 = var()
    f += [
        (h1, R.SMOKES, 'Kools'),
        (h2, R.OWNS, 'horse'),
        (h1, R.NEXT, h2)
    ]
    # 13
    h = var()
    f += [
        (h, R.SMOKES, 'Lucky Strike'),
        (h, R.DRINKS, 'orange juice'),
    ]
    # 14
    h = var()
    f += [
        (h, R.SMOKES, 'Parliaments'),
        (h, R.DRINKS, 'Japanese'),
    ]
    # 15
    h1 = var()
    h2 = var()
    f += [
        (h1, R.WHO, 'Norweigan'),
        (h2, R.COLOR, 'blue'),
        (h1, R.NEXT, h2),
    ]
    return f


def solve(facts):
    for i, f1 in enumerate(facts):
        for f2 in facts[i + 1:]:
            try:
                print(f1, f2)
                unify(f1, f2)
            except ValueError:
                pass


def solution():
    water = var()
    zebra = var()
    h1 = var()
    h2 = var()

    f = facts()
    f +=  [
        (h1, R.DRINKS, 'water'),
        (h1, R.WHO, water),
        (h2, R.OWNS, 'zebra'),
        (h2, R.WHO, zebra)
    ]
    solve(f)

    print('SOLUTION', water, zebra)
