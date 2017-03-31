package secret

const testVersion = 1

var handshakes = [...]string{
	"wink",
	"double blink",
	"close your eyes",
	"jump",
}

func Handshake(code uint) []string {
	var result = make([]string, 0)
	for i := 0; i < len(handshakes); i++ {
		if 1<<uint(i)&code != 0 {
			result = append(result, handshakes[i])
		}
	}
	if 1 << uint(len(handshakes)) & code != 0 {
		reverse(result)
	}
	return result
}

func reverse(slice []string) () {
	for i := 0; i < len(slice)/2; i++ {
		j := len(slice) - i - 1
		slice[i], slice[j] = slice[j], slice[i]
	}
}
