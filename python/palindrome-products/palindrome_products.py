


def smallest_palindrome(max_factor, min_factor=1):
    top = max_factor * max_factor
    bottom = min_factor * min_factor

    for number in range(bottom, top + 1):
        if not _is_palindrome(number):
            continue
        for m in range(min_factor, number):
            d, r = divmod(number, m)
            if d < m:
                break
            elif r:
                continue
            else:
                return number, {m, d}


def largest_palindrome(max_factor, min_factor=1):
    top = max_factor * max_factor
    bottom = min_factor * min_factor

    for number in range(top, bottom, -1):
        if not _is_palindrome(number):
            continue
        for m in range(max_factor, min_factor, -1):
            d, r = divmod(number, m)
            if d > m:
                break
            elif r:
                continue
            else:
                return number, {m, d}


def _is_palindrome(number):
    return str(number) == ''.join(reversed(str(number)))
