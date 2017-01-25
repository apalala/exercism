

def sum_of_multiples(limit, numbers):
    multiples = set(n for n in numbers if n < limit)
    for n in multiples - {0}:
        multiples.update(i * n  for i in range(2, (limit + n - 1) // n))
    return sum(multiples)
