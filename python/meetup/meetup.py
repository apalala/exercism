import calendar
from datetime import date


_WEEKDAY_NUMBER = dict(
    zip(
        calendar.day_name,
        range(len(calendar.day_name))
    )
)
_TEENTH_DAYS = set(range(13, 19 + 1))


class MeetupDayException(Exception):
    pass


def _nth_meetup_day(year, month, weekday, n):
    first_weekday, days_in_month = calendar.monthrange(year, month)

    offset = (7 + weekday - first_weekday) % 7
    day = 1 + offset + (n - 1) * 7

    if day > days_in_month:
        raise MeetupDayException('Meetup day is out of range for month')

    return date(year, month, day)


def _last_meetup_day(year, month, weekday):
    first_weekday, days_in_month = calendar.monthrange(year, month)

    last_weekday = (first_weekday + days_in_month - 1) % 7
    offset = (7 + last_weekday - weekday) % 7

    return date(year, month, days_in_month - offset)


def _teenth_meetup_day(year, month, weekday):
    first_weekday, _ = calendar.monthrange(year, month)

    offset = (7 + weekday - first_weekday) % 7
    day = 1 + offset + 7
    if day not in _TEENTH_DAYS:
        day += 7
        assert day in _TEENTH_DAYS

    return date(year, month, day)


def meetup_day(year, month, weekday_name, which):
    weekday = _WEEKDAY_NUMBER[weekday_name]

    if which == 'last':
        return _last_meetup_day(year, month, weekday)
    elif which == 'teenth':
        return _teenth_meetup_day(year, month, weekday)
    else:
        return _nth_meetup_day(year, month, weekday, int(which[0]))
