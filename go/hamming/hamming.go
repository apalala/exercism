package hamming

import "errors"

const testVersion = 5

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("Sequence lengths differ")
	}

	var distance int
	for i := range a {
		if a[i] != b[i] {
			distance += 1
		}
	}
	return distance, nil
}
