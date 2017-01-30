

CODE = [
    'wink',
    'double blink',
    'close your eyes',
    'jump',
]
REVERSE = len(CODE)


def handshake(code):
    try:
        code = _as_int_code(code)
    except ValueError:
        return []

    codes = [i for i in range(len(CODE)) if (1 << i) & code]
    if (1 << REVERSE) & code:
        codes.reverse()

    return [CODE[c] for c in codes]


def code(words):
    try:
        codes = [CODE.index(w) for w in words]
    except ValueError:
        return '0'

    if codes != sorted(codes):
        codes.append(len(CODE))

    return '{:b}'.format(sum(1 << c for c in codes))


def _as_int_code(code):
    if isinstance(code, str):
        return int(code, 2)
    elif code < 0:
        raise ValueError('Code is negative')
    else:
        return code
