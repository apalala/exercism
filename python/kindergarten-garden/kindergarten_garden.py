

_PLANTS_PER_STUDENT = 2
_PLANTS = [
    'clover',
    'grass',
    'radishes',
    'violets',
]
_PLANT_NAME = {plant[0].upper(): plant.capitalize() for plant in _PLANTS}


_DEFAULT_STUDENTS = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry',
]


class Garden():
    def __init__(self, rows, students=_DEFAULT_STUDENTS):
        self.rows = [list(row) for row in rows.split()]
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student) * _PLANTS_PER_STUDENT
        return [
            _PLANT_NAME[p]
            for row in self.rows
            for p in row[i:i + _PLANTS_PER_STUDENT]
        ]
