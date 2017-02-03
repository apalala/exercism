from copy import deepcopy

WHO = ('Japanese', 'Spaniard', 'Norweigan', 'Ukranian', 'Englishman')
COLOR = ('blue', 'red', 'ivory', 'yellow', 'green')
OWNS = ('dog', 'fox', 'zebra', 'snails', 'horse')
DRINKS = ('milk', 'tea', 'orange juice', 'coffee', 'water')
SMOKES = ('Chesterfield', 'Old Gold', 'Kool', 'Parliament', 'Lucky Strike')


def new_house(n):
    return dict(
        n={n},
        who=set(WHO),
        color=set(COLOR),
        owns=set(OWNS),
        drinks=set(DRINKS),
        smokes=set(SMOKES),
    )


def defined(house):
    values = [len(v) if isinstance(v, set) else 1 for v in house.values()]
    return min(values ) == 1 and max(values) == 1


def remove(house, **kwargs):
    for k, v in kwargs.items():
        if k == 'n':
            continue
        if v in house[k]:
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

def enforce_not(houses, **kwargs):
    return
    for house in houses:
        for ak, av in kwargs.items():
            for bk, bv in kwargs.items():
                if ak == bk:
                    continue
                if av in house[ak] and bv in house[bk]:
                    remove(house, **{ak: av})
                    remove(house, **{bk: bv})


def get(houses, nums, key):
    result = set()
    for i in nums:
        if i >= 0 and i < len(houses):
            result |= houses[i][key]
    return result


def solution():
    # 1
    houses = [new_house(n) for n in range(5)]
    count = 0
    prev = {}
    while houses != prev:
        prev = {}
        while houses != prev:
            prev = deepcopy(houses)
            count += 1
            print(count)
            for i, h in enumerate(houses):
                print(i)
                for v in h.values():
                    print('', v)
            print()
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

        prev ={}
        while houses != prev:
            prev = deepcopy(houses)
            #11
            enforce_not(houses, owns='fox', smokes='Chesterfield')

        for i, house in enumerate(houses):
            for k in set(house) - {'n'}:
                if len(house[k]) == 1:
                    enforce(houses, n=i, **{k: list(house[k])[0]})

        for i, house in enumerate(houses):
            for k in set(house) - {'n'}:
                for v in list(house[k]):
                    where = {j for j, h in enumerate(houses) if v in h[k]}
                    if where == {i} and house[k] != {v}:
                        print(k, v, 'only in', i)
                        house[k] = {v}
                        break
