package diffsquares

const testVersion = 1

func Difference(n int) int {
	return SquareOfSums(n) - SumOfSquares(n)
}

func SquareOfSums(n int) int {
	var sum = n * (n + 1) / 2
	return sum * sum
}

func SumOfSquares(n int) int {
	return int(n * (n + 1) * (2*n + 1) / 6)
}
