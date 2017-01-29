import string
from datetime import datetime


class Robot():

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        now = datetime.now()
        day_of_year = now.timetuple().tm_yday
        day_half = now.hour // 12
        self.name = (
            i2text(day_of_year * day_half, 2)[:2] +
            '%03d' % (now.microsecond // 10 % 1000)
        )


def i2text(value, width=1, alphabet=string.ascii_uppercase):
    n = len(alphabet)
    result = []
    while value != 0:
        value, c = divmod(value, n)
        result.append(alphabet[c])
    np = max(0, width - len(result))
    padding = [alphabet[0]] * np
    return ''.join(padding + result)
