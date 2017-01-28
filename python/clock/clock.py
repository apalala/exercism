

class Clock():
    def __init__(self, hours, minutes):
        self.minute_of_the_day = (hours * 60 + minutes) % (24 * 60)

    def add(self, minutes):
        return Clock(0, self.minute_of_the_day + minutes)

    def _hours_and_minutes(self):
        return (self.minute_of_the_day // 60, self.minute_of_the_day % 60)

    def __hash__(self):
        return hash(self.minute_of_the_day)

    def __eq__(self, other):
        return self.minute_of_the_day == other.minute_of_the_day

    def __str__(self):
        return '%02d:%02d' % self._hours_and_minutes()
