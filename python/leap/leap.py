

def _evenly_divisible(n, m):
    return not n % m


def is_leap_year(year):
    if not _evenly_divisible(year, 4):
        return False
    elif _evenly_divisible(year, 100):
        return _evenly_divisible(year, 400)
    else:
        return True
