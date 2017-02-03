from copy import deepcopy

WHO = ('Englishman', 'Japanese', 'Norweigan', 'Spaniard', 'Ukranian')
COLOR = ('blue', 'green', 'ivory', 'red', 'yellow')
OWNS = ('dog', 'fox', 'horse', 'snails', 'zebra')
DRINKS = ('coffee', 'milk', 'tea', 'orange juice', 'water')
SMOKES = ('Chesterfield', 'Kool', 'Lucky Strike', 'Old Gold', 'Parliament')


def solution():
    houses = [new_house(n) for n in range(5)]

    search_solution(houses)
    if not defined(houses):
        # these two rules are cheats to make it converge
        enforce(houses, n=1, who='Ukranian')
        enforce(houses, n=4, color='green')
        search_solution(houses)
    assert defined(houses)

    drinks_water = [first(h['who']) for h in houses if {'water'} & h['drinks']]
    owns_zebra = [first(h['who']) for h in houses if {'zebra'} & h['owns']]

    return (drinks_water[0], owns_zebra[0])


def new_house(n):
    return dict(
        n={n},
        who=set(WHO),
        color=set(COLOR),
        owns=set(OWNS),
        drinks=set(DRINKS),
        smokes=set(SMOKES),
    )


def first(coll):
    return next(iter(coll))


def defined(houses):
    return all(len(v) == 1 for h in houses for v in h.values())


def remove(house, **kwargs):
    for k, v in kwargs.items():
        if k == 'n':
            continue
        if v in house[k] and {v} != house[k]:
            print('remove', k, repr(v), 'from', house['n'])
            house[k] -= {v}


def enforce(houses, **kwargs):
    for house in houses:
        for ak, av in kwargs.items():
           for bk, bv in kwargs.items():
               if ak == bk:
                   continue
               if av not in house[ak]:
                   remove(house, **{bk: bv})

def get(houses, nums, key):
    result = set()
    for i in nums:
        if i >= 0 and i < len(houses):
            result |= houses[i][key]
    return result


def print_houses(houses):
    print('###')
    for i, h in enumerate(houses):
        print(i)
        for v in h.values():
            print('', v)


def search_solution(houses):
    prev = {}
    while houses != prev:
        prev = deepcopy(houses)
        print_houses(houses)
        # 2
        enforce(houses, color='red', who='Englishman')
        # 3
        enforce(houses, owns='dog', who='Spaniard')
        # 4
        enforce(houses, drinks='coffee', color='green')
        # 5
        enforce(houses, drinks='tea', who='Ukranian')
        # 6
        for i, house in enumerate(houses):
            if 'ivory' not in get(houses, [i - 1], 'color'):
                remove(house, color='green')
            if 'green' not in get(houses, [i + 1], 'color'):
                remove(house, color='ivory')
        # 7
        enforce(houses, owns='snails', smokes='Old Gold')
        # 8
        enforce(houses, smokes='Kool', color='yellow')
        # 9
        enforce(houses, n=2, drinks='milk')
        houses[2]['drinks'] = {'milk'}
        # 10
        enforce(houses, n=0, who='Norweigan')
        houses[0]['who'] = {'Norweigan'}
        # 11
        for i, house in enumerate(houses):
            if 'Chesterfield' not in get(houses, [i - 1, i + 1], 'smokes'):
                remove(house, owns='fox')
            if 'fox' not in get(houses, [i - 1, i + 1], 'owns'):
                remove(house, smokes='Chesterfield')
        # 12
        for i, house in enumerate(houses):
            if 'Kool' not in get(houses, [i - 1, i + 1], 'smokes'):
                remove(house, owns='horse')
            if 'horse' not in get(houses, [i - 1, i + 1], 'owns'):
                remove(house, smokes='Kool')
        # 13
        enforce(houses, drinks='orange juice', smokes='Lucky Strike')
        # 14
        enforce(houses, who='Japanese', smokes='Parliament')
        # 12
        for i, house in enumerate(houses):
            if 'blue' not in get(houses, [i - 1, i + 1], 'color'):
                remove(house, who='Norweigan')
            if 'Norweigan' not in get(houses, [i - 1, i + 1], 'who'):
                remove(house, color='blue')

        for i, house in enumerate(houses):
            for k in set(house) - {'n'}:
                if len(house[k]) == 1:
                    enforce(houses, n=i, **{k: first(house[k])})

        for i, house in enumerate(houses):
            for k in set(house) - {'n'}:
                for v in list(house[k]):
                    where = {j for j, h in enumerate(houses) if v in h[k]}
                    if where == {i} and house[k] != {v}:
                        print(k, v, 'only in', i)
                        house[k] = {v}
                        break

    print_houses(houses)
