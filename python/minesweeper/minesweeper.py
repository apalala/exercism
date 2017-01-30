ARROUND = [
    (-1,-1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def board(matrix):
    def adjust(value):
        if value == ' ':
            return '1'
        elif value.isdigit():
            return str(int(value) + 1)
        else:
            return value

    if not matrix:
        raise ValueError('Empty board')

    m = len(matrix)
    n = len(matrix[0])


    horz_border = '+' + '-' * (n-2) + '+'
    if matrix[0] != horz_border or matrix[m - 1] != horz_border:
        raise ValueError('Corrupt border')
    matrix = [list(row) for row in matrix]

    for i in range(1, m - 1):
        if len(matrix[i]) != n:
            raise ValueError('Rows not of same length')
        if matrix[i][0] != '|' or matrix[i][n - 1] != '|':
            raise ValueError('Corrupt border')

        for j in range(1, n - 1):
            c = matrix[i][j]
            if c not in '* 012345678':
                raise ValueError('Unknown symbol in matrix')
            elif c != '*':
                continue
            else:
                for x, y in ARROUND:
                    matrix[i + x][j + y] = adjust(matrix[i + x][j + y])

    return [''.join(matrix) for matrix in matrix]
