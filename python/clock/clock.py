

class Clock():
    def __init__(self, hours, minutes):
        self.minutes = minutes % 60
        self.hours = (hours + minutes // 60) % 24

    def add(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __hash__(self):
        return self.hours ^ self.minutes

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __str__(self):
        return '%02d:%02d' % (self.hours, self.minutes)
