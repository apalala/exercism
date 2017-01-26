

def sieve(limit):
    numbers = list(range(2, limit + 1))
    not_prime = set()

    for n in numbers:
        if n in not_prime:
            continue
        not_prime.update(n * k for k in range(2, (limit + n) // n))

    return sorted(set(numbers) - not_prime)
