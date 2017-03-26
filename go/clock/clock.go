package clock

import "fmt"

// The value of testVersion here must match `targetTestVersion` in the file
// clock_test.go.
const testVersion = 4

const minutesInDay = 24 * 60

type Clock struct {
	minute_of_the_day int
}

func New(hour, minute int) Clock {
	var minutes = (hour * 60 + minute) % minutesInDay
	if minutes < 0 {
		minutes = minutesInDay + minutes
	}
	return Clock{minutes}
}

func (clock Clock) String() string {
	return fmt.Sprintf("%02d:%02d", clock.Hour(), clock.Minute())
}

func (clock Clock) Add(minutes int) Clock {
	return New(0, clock.minute_of_the_day + minutes)
}

func (clock Clock) Hour() int {
	return clock.minute_of_the_day / 60
}

func (clock Clock) Minute() int {
	return clock.minute_of_the_day % 60
}
