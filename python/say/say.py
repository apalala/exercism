FIRST20 = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nieneteen',
]

TENS = [
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

UNITS = [
    (12, 'trillion'),
    (9, 'billion'),
    (6, 'million'),
    (3, 'thousand'),
    (2, 'hundred'),
]

MAX_NUMBER = 10**UNITS[0][0] - 1


def say(number):
    if number < 0:
        raise AttributeError('Number is negative')
    if number >= MAX_NUMBER:
        raise AttributeError('Number is too large')

    return _say_units(number)


def _say_units(number, units=UNITS):
    spelled = []

    for p, name in units:
        power10 = 10**p
        units_number = number // power10
        number %= power10

        if not units_number:
            continue

        s = _say_units(units_number, units=units[1:])  # generic, so it works with other currencies
        spelled += ['%s %s' % (s, name)]

    if not spelled or number:
        if spelled:
            spelled += ['and']
        spelled += [_say_small_number(number)]

    return ' '.join(spelled)


def _say_small_number(number):
    assert number < 100, number
    number = int(number)

    if number < 20:
        return FIRST20[number]
    elif not number % 10:
        return TENS[number // 10]
    else:
        return TENS[number // 10] + '-' + FIRST20[number % 10]
