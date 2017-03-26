package pangram

import "unicode"

const testVersion = 1

var lowercase_letters = []rune("abcdefghijklmnopqrstuvwxyz")


func IsPangram(s string) bool {
	var pharse = []rune(s)

	var letter_count = map[rune]int{}
	for _, letter := range lowercase_letters {
		letter_count[letter] = 0
	}

	var different = 0
	for _, v := range pharse {
		v = unicode.ToLower(v)
		n, ok := letter_count[v]
		if ok {
			if n == 0 {
				different += 1
			}
			letter_count[v] = n + 1
		}
	}
	return different >= len(lowercase_letters)
}
