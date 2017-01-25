from itertools import islice


def slices(series, n):
    if not n or n > len(series):
        raise ValueError('Length %d is out of range' % n)

    values = [int(c) for c in series]
    substrings = zip(*[islice(values, i, len(values)) for i in range(n)])

    return [list(s) for s in substrings]
