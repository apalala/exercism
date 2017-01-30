

HEX_DIGITS = '0123456789ABCDEF'
HEX_VALUE = {c: i for i, c in enumerate(HEX_DIGITS)}


def hexa(number):
    try:
        return sum(
            HEX_VALUE[c] << i * 4
            for i, c in enumerate(reversed(number.upper()))
        )
    except KeyError:
        raise ValueError('Not a hexadecimal number')