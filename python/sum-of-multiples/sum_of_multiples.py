

def sum_of_multiples(limit, numbers):
    multiples = set(n for n in numbers if n < limit)

    for n in multiples - {0}:
        multiples.update(range(n, limit, n))

    return sum(multiples)
