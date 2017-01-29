

def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('Rows are not of same length')

    colmin = [min(col) for col in zip(*matrix)]
    saddles = set()
    for i, r in enumerate(matrix):
        for j, value in enumerate(r):
            if max(r) <= value <= colmin[j]:
                saddles.add((i, j,))

    return saddles
