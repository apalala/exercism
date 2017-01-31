

class TriangleError(Exception):
    pass


class Triangle():
    def __init__(self, a, b, c):
        if min(a, b, c) <= 0:
            raise TriangleError('Side with negative lenght')
        elif a + b + c <= 2 * max(a, b, c):
            raise TriangleError('Not a triangle')

        self.a, self.b, self.c = a, b, c
        self.sides = {a, b, c}

    def kind(self):
        n = len(self.sides)
        if n == 1:
            return 'equilateral'
        elif n == 2:
            return 'isosceles'
        else:
            return 'scalene'
