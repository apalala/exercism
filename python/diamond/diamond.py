import string

LETTERS = string.ascii_uppercase


def make_diamond(letter):
    n = LETTERS.index(letter)
    m = 2 * n + 1

    letters = LETTERS[:n + 1]

    rows = []
    for i, c in enumerate(letters):
        row = [' '] * m
        row[n + i] = row[n - i] = c
        rows.append(''.join(row))
    rows.extend(reversed(rows[:-1]))

    return '\n'.join(rows) + '\n'