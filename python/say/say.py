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


def say(number):
    if number < 0:
        raise AttributeError('Number is negative')
    if number >= 10**12 - 1:
        raise AttributeError('Number is too large')

    spelled = ''

    billions = number // 10**9
    number %= 10**9
    if billions:
        spelled += say(billions) + ' billion '

    millions = number // 10**6
    number %= 10**6
    if millions:
        spelled += say(millions) + ' million '

    thousands = number // 10**3
    number %= 10**3
    if thousands:
        spelled += say(thousands) + ' thousand '

    hundreds = number // 10**2
    number %= 10**2
    if hundreds:
        spelled += say(hundreds) + ' hundred '

    if not spelled or number:
        if spelled:
            spelled += 'and '
        spelled += say_small(number)

    return spelled.strip()


def say_small(number):
    assert number < 100, number
    number = int(number)

    if number < 20:
        return FIRST20[number]
    if not number % 10:
        return TENS[number // 10]
    return TENS[number // 10] + '-' + FIRST20[number % 10]
