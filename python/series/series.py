from itertools import islice


def slices(series, n):
    if not n or n > len(series):
        raise ValueError('Length %d is out of range' % n)

    return [
        [int(i) for i in s]
        for s in zip(*[islice(series, i, len(series)) for i in range(n)])
    ]
