
BAD_NUMBER = '0'*10

class Phone():
    def __init__(self, number):
        digits = ''.join(d for d in number if d.isdigit())

        n = len(digits)

        if n < 10 or n == 11 and digits[0] != '1':
            self.number = BAD_NUMBER
        elif n == 11:
            self.number = digits[1:]
        else:
            self.number = digits

    def pretty(self):
        n = self.number
        return '(%s) %s-%s' % (n[:3], n[3:6], n[6:])

    def area_code(self):
        return self.number[:3]
