# after studying solution by @iltrof on EXERCISM
# optimized with `yield from` instead of list concatenations
from math import sqrt


def prime_factors(number):
    def factors(n):
        if n < 2:
            return

        if n % 2 == 0:
            yield 2
            yield from factors(n // 2)
            return

        for p in range(3, int(sqrt(n)) + 1, 2):
            quotient, remainder = divmod(n, p)
            if remainder:
                continue
            yield p
            yield from factors(quotient)
            break
        else:
            yield n

    return list(factors(number))
