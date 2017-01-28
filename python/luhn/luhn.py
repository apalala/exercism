

class Luhn():
    def __init__(self, code):
        self.code = code

    @classmethod
    def _addends(cls, code):
        digits = list(reversed([int(c) for c in str(code)]))
        return [
            d if d == 9 or not i % 2 else (2 * d) % 9
            for i, d in enumerate(digits)
        ]

    def addends(self):
        return self._addends(self.code)

    @classmethod
    def _checksum(cls, code):
        return sum(cls._addends(code))

    def checksum(self):
        return self._checksum(self.code)

    @classmethod
    def _is_valid(cls, code):
        return cls._checksum(code) % 10 == 0

    def is_valid(self):
        print(self.addends())
        return self._is_valid(self.code)

    @classmethod
    def create(cls, code):
        if cls._is_valid(code):
            return code

        code *= 10
        cs = cls._checksum(code) % 10
        return code + (10 - cs) % 10

