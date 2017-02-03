

def count(diagram=None):
    if not diagram:
        return 0

    vertex = {
        (i, j) for i, row in enumerate(diagram)
        for j, v in enumerate(row)
        if v == '+'
    }

    candidates = {
        tuple(sorted([a, b, c, d]))
        for a in vertex
        for b in vertex - {a} if a[0] == b[0]
        for c in vertex - {a, b} if c[1] == a[1]
        for d in vertex - {a, b, c} if d[0] == c[0] and d[1] == b[1]
    }


    rectangles = [
        (a, b, c, d)
        for a, b, c, d in candidates
        if (
            _connected(diagram, a, b) and
            _connected(diagram, c, d) and
            _connected(diagram, a, c) and
            _connected(diagram, b, d)
        )
    ]

    return len(rectangles)


def _connected(diagram, a, b):
    (ia, ja), (ib, jb) = sorted((a, b))
    assert diagram[ia][ja] == '+'
    assert diagram[ib][jb] == '+'
    if ia == ib:
        return {'+', '-'} == {diagram[ia][j] for j in range(ja, jb + 1)}
    elif ja == jb:
        return {'+', '|'} == {diagram[i][ja] for i in range(ia, ib + 1)}
    else:
        return False
