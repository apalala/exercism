

CODE = [
    'wink',
    'double blink',
    'close your eyes',
    'jump',
]

REVERSE_CODE = {name: i for i, name in enumerate(CODE)}


def handshake(code):
    if isinstance(code, str):
        if not all(d in '01' for d in code):
            return []
        code = int(code, 2)
    if code < 0:
        return []

    names = []
    for i, name in enumerate(CODE):
        if (1 << i) & code:
            names.append(name)
    if (1 << 4) & code:
        names = names.reverse()
    return names


def code(words):
    value = 0
    for name in words:
        value |= REVERSE_CODE.get(name, 0)
    return str(value)


