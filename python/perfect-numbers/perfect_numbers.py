

def is_perfect(number):
    return number == sum(_factors(number))


def _factors(number):
    factors = {1}
    for f in range(2, number):
        if f in factors:
            break
        d, r = divmod(number, f)
        if r == 0:
            factors.update([f, d])
    return factors
