
def board(w, b):
    (wr, wc), (br, bc) = w, b

    if w == b:
        raise ValueError('Both queens in same position')
    if max(wr, wc, br, bc) >= 8:
        raise ValueError('Position outside board')

    t = [['_'] * 8 for _ in range(8)]
    t[wr][wc] = 'W'
    t[br][bc] = 'B'

    return [''.join(row) for row in t]


def can_attack(w, b):
    (wr, wc), (br, bc) = w, b

    if w == b:
        raise ValueError('Both queens in same position')
    if max(wr, wc, br, bc) >= 8:
        raise ValueError('Position outside board')

    return (
        wr == br or
        wc == bc or
        wr - wc == br - bc or
        wr - br == bc - wc
    )
