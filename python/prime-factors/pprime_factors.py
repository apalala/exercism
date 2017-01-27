# after studying solution by @iltrof on EXERCISM
# optimized with `yield from` instead of list concatenations
from math import sqrt
from itertools import takewhile

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


def prime_factors(number):
    for i in range(10000):
        _prime_factors(number)
    return _prime_factors(number)


def _prime_factors(number):
    def factors(n):
        if n < 2:
            return

        if n % 2 == 0:
            yield 2
            yield from factors(n // 2)
            return

        for p in _primes_upto(int(sqrt(n))):
            quotient, remainder = divmod(n, p)
            if remainder:
                continue
            yield p
            yield from factors(quotient)
            break
        else:
            yield n

    return list(factors(number))


def _primes_upto(limit):
    known_primes = takewhile(lambda p: p <= limit, __primes)
    yield from known_primes

    last_prime = __primes[-1]
    for n in range(last_prime + 2, limit + 1, 2):
        if not _is_prime(n):
            continue

        __primes.append(n)
        yield n


def _is_prime(number):
    return all(number % p for p in _primes_upto(int(sqrt(number))))
