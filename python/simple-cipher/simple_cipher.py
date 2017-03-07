from itertools import cycle
import string

_N = len(string.ascii_lowercase)


def _num(text):
    return [ord(c) - ord('a') for c in text.lower() if c.isalpha()]


def _alpha(digits):
    return ''.join(chr(d + ord('a')) for d in digits)


class Cipher():
    def __init__(self, key='x' * 100):
        if not key.isalpha() or not key.islower():
            raise ValueError('Key must be alphabetic lowercase')
        self.key = key

    def encode(self, text):
        cypher = _num(text)
        keys = cycle(_num(self.key))
        print([next(keys) for _ in range(2 * len(self.key))])
        return _alpha((d + k) % _N for d, k in zip(cypher, keys))

    def decode(self, cypher):
        cypher = _num(cypher)
        keys = cycle(_num(self.key))
        return _alpha((d - k) % _N for d, k in zip(cypher, keys))


class Caesar(Cipher):
    def __init__(self):
        super().__init__('dddd')
