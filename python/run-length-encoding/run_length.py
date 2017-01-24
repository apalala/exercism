import re
from itertools import groupby

def encode(text):
    seqs = [''.join(g) for _, g in groupby(text)]
    result = []
    for seq in seqs:
        if len(seq) == 1:
            result.append(seq)
        else:
            result.append('%d%s' % (len(seq), seq[0]))
    return ''.join(result)


def decode(text):
    code_char = re.split('(\D)', text)[1:]
    print(code_char)
    it = iter(code_char)
    return ''.join(int(n) * c for n, c in zip(it, it))
