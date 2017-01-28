

class School():
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add(self, student, n):
        if n > len(self.grades):
            self.grades += [set() for _ in range(n - len(self.grades))]
        self.grades[n - 1].add(student)

    def grade(self, n):
        if n > len(self.grades):
            return ()
        return tuple(sorted(self.grades[n - 1]))

    def sort(self):
        return [
            (n, self.grade(n))
            for n in range(1, len(self.grades) + 1)
            if self.grades[n - 1]
        ]
