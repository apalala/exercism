

def _evenly_divisible(n, m):
    return not n % m


def is_leap_year(year):
    return (
        _evenly_divisible(year, 400) or
        _evenly_divisible(year, 4) and not _evenly_divisible(year, 100)
    )
