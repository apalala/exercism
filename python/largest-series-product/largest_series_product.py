from itertools import islice
from functools import reduce
from operator import __mul__


def largest_product(series, size):
    if size < 0:
        raise ValueError('Size is negative')
    elif len(series) < size:
        raise ValueError('Series is too short')
    elif not series or not size:
        return 1
    else:
        values = [int(d) for d in series]
        return max(
            _multiply(islice(values, i, i + size))
            for i in range(1 + len(series) - size)
        )


def _multiply(values):
    return reduce(__mul__, values, 1)
