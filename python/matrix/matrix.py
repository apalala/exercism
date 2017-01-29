

class Matrix():
    def __init__(self, astext):
        self.rows = [
            [int(value) for value in row.split()]
            for row in astext.split('\n')
            ]
        self.columns = list(list(col) for col in zip(*self.rows))