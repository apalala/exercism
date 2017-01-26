

def sum_of_multiples(limit, numbers):
    return sum({i for n in numbers if n for i in range(n, limit, n)})
