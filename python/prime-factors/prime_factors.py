# after studying solution by @iltrof on EXERCISM
from math import sqrt


def prime_factors(number):
    if number < 2:
        return []
    elif number % 2 == 0:
        return [2] + prime_factors(number // 2)
    else:
        for p in range(3, int(sqrt(number)) + 1, 2):
            quotient, remainder = divmod(number, p)
            if remainder:
                continue
            return [p] + prime_factors(quotient)

        return [number]
