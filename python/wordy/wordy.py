import re
from operator import __add__, __sub__, __mul__, __floordiv__


OPS = {
    'plus': __add__,
    'minus': __sub__,
    'multiplied by': __mul__,
    'divided by': __floordiv__,
}


def calculate(operation):
    parts = re.split('([\d+-]+)', operation.lower().rstrip('?'))
    parts = [p.strip() for p in parts[1:] if p]
    print(parts)

    numbers = [int(p) for p in parts if _is_number(p)]
    ops = [p for p in parts if not _is_number(p)]

    result = numbers[0]
    i = 1
    for o in ops:
        if o not in OPS:
            raise ValueError('Unknown operation %s' % o)
        result = OPS[o](result, numbers[i])
        i += 1
    return result


def _is_number(s):
    return s.isnumeric() or s[0:1] in '+-' and s[1:].isnumeric()

