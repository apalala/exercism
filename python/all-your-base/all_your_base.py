

def rebase(base, digits, new_base):
    if base <= 1:
        raise ValueError('Base is <= 1')
    if new_base <= 1:
        raise ValueError('New base is <= 1')
    if any(d >= base or d < 0 for d in digits):
        raise ValueError('Invalid digit')

    def _rebase(number, base):
        result = []
        while number:
            number, digit = divmod(number, base)
            result.append(digit)
        return list(reversed(result))

    decimal = sum(d * base**i for i, d in enumerate(reversed(digits)))
    return _rebase(decimal, new_base)
