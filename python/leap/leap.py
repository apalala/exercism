

def _divisible(n, m):
    return not n % m


def is_leap_year(year):
    return (
        _divisible(year, 400) or
        _divisible(year, 4) and not _divisible(year, 100)
    )
