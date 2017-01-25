import calendar
from datetime import date
from datetime import timedelta


WEEKDAY_NUMBER = dict(zip(calendar.day_name, range(len(calendar.day_name))))
TEENTH_DAYS = set(range(13, 20))


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday_name, kind):
    first_of_month = date(year=year, month=month, day=1)
    weekday = WEEKDAY_NUMBER[weekday_name]

    first_weekday, days_in_month = calendar.monthrange(year, month)
    target_days = set(range(1 + days_in_month))
    offset = (7 + weekday - first_weekday) % 7

    if kind == 'last':
        weeks = [5, 4, 3]
    elif kind == 'teenth':
        weeks = [1, 2]
        target_days = TEENTH_DAYS
    else:
        weeks = [int(kind[0]) - 1]

    for week in weeks:
        result = first_of_month + timedelta(days=offset + week * 7)
        if result.month == month and result.day in target_days:
            return result

    raise MeetupDayException('Cannot find {} {} in {}/'.format(kind, weekday_name, month, year))

