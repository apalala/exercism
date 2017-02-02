from enum import IntEnum
from itertools import count


class R(IntEnum):
    NUMBER = 0
    WHO = 1
    COLOR = 2
    OWNS = 3
    DRINKS = 4
    SMOKES = 5

    RIGHT = 6
    NEXT = 7


def _error(a, b):
    raise ValueError('Cannot unify %s with %s' % (a, b))


class Var():
    counter = count()

    def __init__(self, value=None):
        self.id = next(self.counter)
        self._value = value

    @property
    def value(self):
        if self._value is None:
            return None
        elif isinstance(self._value, Var):
            return self._value.value
        else:
            return self._value

    @value.setter
    def value(self, value):
        print('set', self, self._value, value)
        assert self.value is None
        self._value = value

    def __eq__(self, other):
        return (
            super().__eq__(other) or
            self._value == other or
            self._value == other.value
        )

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        if self._value is not None:
            return 'v%d->%s' % (self.id, repr(self._value))
        else:
            return 'v%d' % self.id


def var(value=None):
    return Var(value=value)


def unify_atom(a, b):
    if a == b:
        pass
    elif isinstance(a, Var) and a.value is None:
        a.value = b
    elif isinstance(b, Var) and b.value is None:
        b.value = a
    else:
        return a == b
    return True


def unify(a, b):
    return a[0] == b[0] and unify_atom(a[2], b[2]) and unify_atom(a[1], b[1])


def solve(facts):
    facts = sorted(facts)
    for i, f in enumerate(facts):
        if f[0] == R.NEXT:
            continue
        for g in facts[i + 1:]:
            if g[0] == R.NEXT:
                continue
            try:
                # print(f, g)
                unify(f, g)
            except ValueError:
                pass
    for i in range(5):
        for f in facts:
            unify(f, (R.NEXT, i, i + 1))
            unify(f, (R.NEXT, i + 1, i))


def solution():
    water = var()
    zebra = var()

    f, homes = facts()
    f += [
        (R.DRINKS, water, 'water'),
        (R.OWNS, zebra, 'zebra'),
    ]
    solve(f)
    for fact in f:
        print('(%s, %s, %s)' % fact)

    print('SOLUTION', water, zebra)


def facts():
    # 1
    facts = []
    homes = [var(i) for i in range(5)]
    facts += [
        (R.RIGHT,var(0), 1),
        (R.RIGHT,var(1), 2),
        (R.RIGHT,var(2), 3),
        (R.RIGHT,var(3), 4),
    ]
    # 2
    h = var()
    facts += [
        (R.WHO, h, 'Englishman'),
        (R.COLOR, h, 'red'),
    ]
    # 3
    h = var()
    facts += [
        (R.WHO, h, 'Spaniard'),
        (R.OWNS, h, 'dog'),
    ]
    # 4
    h = var()
    facts += [
        (R.DRINKS, h, 'coffee'),
        (R.COLOR, h, 'green'),
    ]
    # 5
    h = var()
    facts += [
        (R.WHO, h, 'Ukranian'),
        (R.DRINKS, h, 'tea'),
    ]
    # 6
    h1 = var()
    h2 = var()
    facts += [
        (R.COLOR, h1, 'ivory'),
        (R.COLOR, h2, 'green'),
        (R.RIGHT, h1, h2),
    ]
    # 7
    h = var()
    facts += [
        (R.SMOKES, h, 'Old Gold'),
        (R.OWNS, h, 'snails'),
    ]
    # 8
    h = var()
    facts += [
        (R.COLOR, h, 'yellow'),
        (R.SMOKES, h, 'Kools'),
    ]
    # 9
    h = var()
    facts += [
        (R.DRINKS,var(2), 'milk'),
    ]
    # 10
    h = var()
    facts += [
        (R.WHO,var(0), 'Norweigan'),
    ]
    # 11
    h1 = var()
    h2 = var()
    facts += [
        (R.SMOKES, h1, 'Chesterfields'),
        (R.OWNS, h2, 'fox'),
        (R.NEXT, h1, h2)
    ]
    # 12
    h1 = var()
    h2 = var()
    facts += [
        (R.SMOKES, h1, 'Kools'),
        (R.OWNS, h2, 'horse'),
        (R.NEXT, h1, h2)
    ]
    # 13
    h = var()
    facts += [
        (R.SMOKES, h, 'Lucky Strike'),
        (R.DRINKS, h, 'orange juice'),
    ]
    # 14
    h = var()
    facts += [
        (R.SMOKES, h, 'Parliaments'),
        (R.DRINKS, h, 'Japanese'),
    ]
    # 15
    h1 = var()
    h2 = var()
    facts += [
        (R.WHO, h1, 'Norweigan'),
        (R.COLOR, h2, 'blue'),
        (R.NEXT, h1, h2),
    ]
    return facts, homes
