

def sieve(limit):
    numbers = list(range(2, limit + 1))

    not_prime = set()
    for n in numbers:
        if n in not_prime:
            continue
        not_prime.update(range(2 * n, limit + 1, n))

    return sorted(set(numbers) - not_prime)
