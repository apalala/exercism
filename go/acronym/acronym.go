package acronym

import "unicode"

const testVersion = 2

func Abbreviate(s string) string {
	var words = _words(s)
	var result []rune
	for _, w := range words {
		result = append(result, unicode.ToUpper(w[0]))
	}
	return string(result)
}

func _words(s string) [][]rune {
	var phrase = []rune(s)
	var result [][]rune
	var i = 0
	for i < len(phrase) {
		if !unicode.IsLetter(phrase[i]) {
			i += 1
		} else {
			var j = i
			for j < len(phrase) && unicode.IsUpper(phrase[j]) {
				j += 1
			}
			for j < len(phrase) && unicode.IsLower(phrase[j]) {
				j += 1
			}
			result = append(result, phrase[i:j])
			i = j
		}
	}
	return result
}
