from enum import IntEnum
from itertools import count
from collections import defaultdict
from copy import copy


class R(IntEnum):
    NUMBER = 10
    WHO = 11
    COLOR = 12
    OWNS = 13
    DRINKS = 14
    SMOKES = 15

    RIGHT = 6
    NEXT = 17


class UnificationError(ValueError):
    pass


class Val():
    counter = count(1)
    atoms = {}

    @classmethod
    def val(cls, value):
        if isinstance(value, Val):
            return value
        elif value is None:
            return Val()
        elif not value in cls.atoms:
            cls.atoms[value] = Val(value)
        return cls.atoms[value]

    def __init__(self, value=None):
        self.id = next(self.counter)
        self._value = value

    @property
    def value(self):
        if self._value is None:
            return None
        elif isinstance(self._value, Val):
            return self._value.value
        else:
            return self._value

    @value.setter
    def value(self, value):
        assert self.value is None
        v = self
        while v._value is not None:
            v = v._value
        v._value = value

    def __eq__(self, other):
        return isinstance(other, Val) and self.value == other.value

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        if self._value is None:
            return '[%d]' % self.id
        else:
            return '[%d]->%s' % (self.id, repr(self._value))


class Var():
    counter = count(1)

    def __init__(self, value=None):
        self.id = next(self.counter)

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return (
            super().__eq__(other) or
            self.id == other.id
        )

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return 'v%d' % self.id


class Ctx(dict):
    def __getitem__(self, item):
        if not isinstance(item, Var):
            return item
        value = super().__getitem__(item)
        assert isinstance(value, Val), value
        return value

    def __missing__(self, key):
        if not isinstance(key, Var):
            return key
        self[key] = Val()
        return self[key]

    def copy(self):
        ctx = Ctx()
        ctx.update(self)
        return ctx


def _error(a, b):
    raise UnificationError('Cannot unify %s with %s' % (a, b))


def val(value=None):
    return Val.val(value)


def var():
    return Var()


def tprint(ctx, tag, *args):
    print(tag, *(tuple([ctx[v] for v in a]) for a in args))


def unify_atom(ctx, a, b):
    if a == b:
        pass
    elif isinstance(a, Var) and ctx[a].value is None:
        ctx[a].value = ctx[b]
        assert isinstance(ctx[a], Val)
    elif isinstance(b, Var) and ctx[b].value is None:
        ctx[b].value = ctx[a]
        assert isinstance(ctx[b], Val)
    else:
        return ctx[a] == ctx[b]
    return True


def unify(ctx, a, b):
    if a[0] != b[0]:
        return ctx

    ctx = ctx.copy()
    unified = (
        a[0] == b[0] and
        unify_atom(ctx, a[2], b[2]) and
        unify_atom(ctx, a[1], b[1])
    )
    if unified:
        return ctx
    else:
        _error(a, b)


def solve(facts):
    ctx = Ctx()
    facts = sorted(facts)
    for i, f in enumerate(facts):
        for g in facts[i + 1:]:
            if f[0] != g[0]:
                continue
            if g[0] == R.NEXT:
                continue
            try:
                tprint(ctx, '>>>', f, g)
                ctx = unify(ctx, f, g)
                tprint(ctx, '<<<', f, g)
            except UnificationError:
                pass
    for i in range(5):
        for f in facts:
            try:
                ctx = unify(ctx, f, (R.NEXT, val(i), val(i + 1)))
            except UnificationError:
                pass
            try:
                ctx = unify(ctx, f, (R.NEXT, val(i + 1), val(i)))
            except UnificationError:
                pass
    return ctx


def solution():
    water = var()
    zebra = var()

    f = known_facts()
    f += [
        (R.DRINKS, water, val('water')),
        (R.OWNS, zebra, val('zebra')),
    ]
    ctx = solve(f)
    for fact in f:
        a, b, c = fact
        print('(%s, %s, %s)' % (ctx[a], ctx[b], ctx[c]))

    drinks = [(ctx[b].value, ctx[c].value) for a, b, c in f if a == R.DRINKS]
    print('DRINKS', drinks)
    owns = [(ctx[b].value, ctx[c].value) for a, b, c in f if a == R.OWNS]
    print('OWNS', owns)
    print('SOLUTION', ctx[water], ctx[zebra])


def known_facts():
    # 1
    facts = []
    facts += [
        (R.RIGHT, val(0), val(1)),
        (R.RIGHT, val(1), val(2)),
        (R.RIGHT, val(2), val(3)),
        (R.RIGHT, val(3), val(4)),
    ]
    # 2
    h = var()
    facts += [
        (R.WHO, h, val('Englishman')),
        (R.COLOR, h, val('red')),
    ]
    # 3
    h = var()
    facts += [
        (R.WHO, h, val('Spaniard')),
        (R.OWNS, h, val('dog')),
    ]
    # 4
    h = var()
    facts += [
        (R.DRINKS, h, val('coffee')),
        (R.COLOR, h, val('green')),
    ]
    # 5
    h = var()
    facts += [
        (R.WHO, h, val('Ukranian')),
        (R.DRINKS, h, val('tea')),
    ]
    # 6
    h1 = var()
    h2 = var()
    facts += [
        (R.COLOR, h1, val('ivory')),
        (R.COLOR, h2, val('green')),
        (R.RIGHT, h1, h2),
    ]
    # 7
    h = var()
    facts += [
        (R.SMOKES, h, val('Old Gold')),
        (R.OWNS, h, val('snails')),
    ]
    # 8
    h = var()
    facts += [
        (R.COLOR, h, val('yellow')),
        (R.SMOKES, h, val('Kools')),
    ]
    # 9
    h = var()
    facts += [
        (R.DRINKS, val(2), val('milk')),
    ]
    # 10
    h = var()
    facts += [
        (R.WHO, val(0), val('Norweigan')),
    ]
    # 11
    h1 = var()
    h2 = var()
    facts += [
        (R.SMOKES, h1, val('Chesterfields')),
        (R.OWNS, h2, val('fox')),
        (R.NEXT, h1, h2)
    ]
    # 12
    h1 = var()
    h2 = var()
    facts += [
        (R.SMOKES, h1, val('Kools')),
        (R.OWNS, h2, val('horse')),
        (R.NEXT, h1, h2),
    ]
    # 13
    h = var()
    facts += [
        (R.SMOKES, h, val('Lucky Strike')),
        (R.DRINKS, h, val('orange juice')),
    ]
    # 14
    h = var()
    facts += [
        (R.SMOKES, h, val('Parliaments')),
        (R.WHO, h, val('Japanese')),
    ]
    # 15
    h1 = var()
    h2 = var()
    facts += [
        (R.WHO, h1, val('Norweigan')),
        (R.COLOR, h2, val('blue')),
        (R.NEXT, h1, h2),
    ]
    return facts
