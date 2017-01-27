

def sieve(limit):
    numbers = [2] + list(range(3, limit + 1, 2))

    not_prime = set()
    for n in numbers:
        if n in not_prime:
            continue
        not_prime.update(range(3 * n, limit + 1, 2 * n))

    return sorted(set(numbers) - not_prime)
