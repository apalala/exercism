from math import sqrt
from itertools import zip_longest


def encode(text):
    text = [c for c in text.lower() if c.isalnum()]

    s = sqrt(len(text))
    r = int(s)
    c = r if r == s else r + 1
    assert (c - r) <= 1

    rows = zip_longest(*[iter(text)] * c, fillvalue=' ')
    columns = zip(*rows)

    return ' '.join(
        ''.join(column).strip()
        for column in columns
    )