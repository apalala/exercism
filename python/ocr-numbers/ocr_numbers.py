

_ALL_GRIDS = [
    ' _     _  _     _  _  _  _  _ ',
    '| |  | _| _||_||_ |_   ||_||_|',
    '|_|  ||_  _|  | _||_|  ||_| _|',
    '                              ',
]


def _chunks(seq, n):
    return [''.join(chunk) for chunk in zip(*[iter(seq)] * n)]


def _split_grid(grid):
    if len(grid) != len(_ALL_GRIDS):
        raise ValueError('Incorrectly shaped grid')
    elif any(len(row) != len(grid[0]) for row in grid):
        raise ValueError('Incorrectly shaped grid')
    else:
        rows = [_chunks(row, 3) for row in grid]
        return ['\n'.join(n) for n in zip(*rows)]


_GRIDS = _split_grid(_ALL_GRIDS)


def number(grid):
    values = {m: str(i) for i, m in enumerate(_GRIDS)}
    return ''.join(
        values.get(digit, '?')
        for digit in _split_grid(grid)
    )


def grid(number):
    grids = {str(i): m for i, m in enumerate(_GRIDS)}
    try:
        return [
            ''.join(row)
            for row in zip(*[
                grids[digit].split('\n')
                for digit in number
            ])
        ]
    except KeyError:
        raise ValueError('Unknown digit')
