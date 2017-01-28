from math import sqrt


def primitive_triplets(b):
    def triplets():
        for n in range(1, b):
            m = b / (2 * n)
            if m < n:
                break
            elif m != int(m):
                continue
            elif _mcd(n, int(m)) != 1:
                continue
            else:
                m = int(m)
                assert b == 2 * n * m

                a = m * m - n * n
                c = m * m + n * n
                assert c**2 == a**2 + b**2

                yield tuple(sorted((a, b, c)))

    if b % 2 != 0:
        raise ValueError('Argument must be even')
    return set(triplets())


def triplets_in_range(low, high):
    def triplets():
        for a in range(low, high):
            for b in range(a + 1, high):
                c = sqrt(a**2 + b**2)
                if c > high:
                    break
                elif c != int(c):
                    continue
                else:
                    c = int(c)
                    assert c**2 == a**2 + b**2
                    yield (a, b, c)
    return set(triplets())


def is_triplet(triplet):
    return (
        len(triplet) == 3 and
        2 * max(triplet)**2 == sum(x**2 for x in triplet)
    )


def _mcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a