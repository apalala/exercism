from itertools import islice


def slices(series, n):
    if not n or n > len(series):
        raise ValueError('Length %d is out of range' % n)

    substrings = zip(*[islice(series, i, len(series)) for i in range(n)])

    return [[int(c) for c in s] for s in substrings]
