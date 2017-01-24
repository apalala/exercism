from datetime import datetime
from datetime import timedelta

_GIGASECOND = timedelta(0, 10**9)

def add_gigasecond(birthday):
    return birthday + _GIGASECOND