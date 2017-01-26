import string
from itertools import zip_longest


CODE = dict(zip(string.ascii_lowercase, reversed(string.ascii_lowercase)))


def _flip(c):
    return CODE.get(c, c) if c.isalnum() else ''


def encode(text):
    ciphertext = ''.join(_flip(c) for c in text.lower())

    chunks_of_5 = zip_longest(*[iter(ciphertext)] * 5, fillvalue='')

    return ' '.join(''.join(chunk) for chunk in chunks_of_5)


def decode(text):
    return ''.join(_flip(c) for c in text)
