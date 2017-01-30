

def parse_binary(n):
    if not set(n) <= {'0', '1'}:
        raise ValueError('Must be all 0s and 1s')
    return sum(
        1 << i
        for i, c in enumerate(reversed(n))
        if c == '1'
    )
