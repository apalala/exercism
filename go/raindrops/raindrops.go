package raindrops

import "strconv"

const testVersion = 2

func Convert(n int) string {
	var output = ""
	if n % 3 == 0 {
		output += "Pling"
	}
	if n % 5 == 0 {
		output += "Plang"
	}
	if n % 7 == 0 {
		output += "Plong"
	}
	if output == "" {
		return strconv.Itoa(n)
	}
	return output
}

