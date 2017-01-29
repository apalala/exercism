from math import sqrt
from bisect import bisect_left
from itertools import count
from itertools import takewhile
from itertools import islice

__primes = [
    2, 3, 5, 7,
    11, 13, 17, 19,
    23, 29,
    31, 37,
    41, 43, 47,
    53, 59,
    61, 67,
    71, 73, 79,
    83, 89,
    97
]


def nth_prime(n):
    for _ in _more_primes(n):
        pass
    return __primes[n - 1]


def _primes():
    yield from __primes
    yield from _more_primes()


def _more_primes(n=None):
    for p in count(__primes[-1] + 2, 2):
        if n and len(__primes) >= n:
            return
        elif not _is_prime(p):
            continue
        else:
            __primes.append(p)
            yield p


def _primes_upto(limit):
    yield from takewhile(lambda p: p <= limit, _primes())


def _is_prime(number):
    if number > __primes[-1]:
        return all(number % p for p in _primes_upto(int(sqrt(number))))
    else:
        i = bisect_left(__primes, number)
        return __primes[i] == number
