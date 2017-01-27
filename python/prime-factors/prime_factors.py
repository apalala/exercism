from itertools import takewhile
from math import sqrt


_CACHED_PRIMES = [2, 3, 5, 7]


def prime_factors (number):
    if number < 2:
        return []

    factors = []

    primes = _primes_upto(number)
    p = next(primes)
    while number >= p:
        if number == p or _is_prime(number):
            factors.append(number)
            break

        quotient, remainder = divmod(number, p)
        if remainder:
            p = next(primes)
        else:
            factors.append(p)
            number = quotient

    return factors


def _primes_upto(limit):
    known_primes = takewhile(lambda p: p <= limit, _CACHED_PRIMES)
    yield from known_primes

    last_prime = _CACHED_PRIMES[-1]
    for n in range(last_prime + 2, limit + 1, 2):
        if not _is_prime(n):
            continue

        _CACHED_PRIMES.append(n)
        yield n


def _is_prime(number):
    return all(number % p for p in _primes_upto(int(sqrt(number))))
