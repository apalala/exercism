package leap

const testVersion = 3

// IsLeapYear determines if a year is a leap year
func IsLeapYear(year int) bool {
	return multiple(year, 400) || multiple(year, 4) && !multiple(year, 100)
}

func multiple(n, m int) bool {
	return n%m == 0
}
