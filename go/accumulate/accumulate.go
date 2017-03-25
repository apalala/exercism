package accumulate

var testVersion = 1

func Accumulate(values []string, convert func(string) string) (result []string) {
	result = make([]string, len(values))
	for i := range values {
		result[i] = convert(values[i])
	}
	return
}
