

def encode(text, nrails):
    rails = [''] * nrails
    for c, i in zip(text, _zigzag(nrails)):
        rails[i] += c
    return ''.join(rails)


def decode(cipher, nrails):
    pattern = list(_zigzag(nrails, len(cipher)))

    rails = [[] for _ in range(nrails)]
    for i, c in zip(sorted(pattern), cipher):
        rails[i] = [c] + rails[i]

    return ''.join(rails[i].pop() for i in pattern)


def _zigzag(n, limit=None):
    i = 0
    while limit is None or limit:
        yield abs(i)
        if i + 1 < n:
            i += 1
        else:
            i = -i + 1

        if limit:
            limit -=1
