package bob

import (
	"strings"
	"unicode"
)

const testVersion = 2


func Hey(what string) string {
	what = strings.TrimSpace(what)
	var rwhat = []rune(what)

	if len(what) == 0 {
		return "Fine. Be that way!"
	}

	var all_upper = true
	var has_letters = false
	for _, v := range rwhat {
		if unicode.IsLetter(v) {
			has_letters = true
			if !unicode.IsUpper(v) {
				all_upper = false
				break
			}
		}
	}
	if has_letters && all_upper {
		return "Whoa, chill out!"
	}

	if rwhat[len(rwhat) - 1] == []rune("?")[0] {
		return "Sure."
	}

	return "Whatever."

}
