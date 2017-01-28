import re
from itertools import groupby

def encode(text):
    seqs = [''.join(g) for _, g in groupby(text)]

    codes = [(str(len(s)) if len(s) > 1 else '', s[0]) for s in seqs]

    return ''.join('%s%s' % (n, c) for n, c in codes)


def decode(text):
    code_char = re.findall('\d*\D', text)

    codes = [(c[:-1], c[-1]) for c in code_char]

    return ''.join(int(n or '1') * c for n, c in codes)
