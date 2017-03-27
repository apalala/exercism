package diffsquares

import "math"

const testVersion = 1

func Difference(n int) int {
	return SquareOfSums(n) - SumOfSquares(n)
}

func SquareOfSums(n int) int {
	var x = float64(n)
	return int(math.Pow(x*(x+1)/2, 2))
}

func SumOfSquares(n int) int {
	return int(n * (n + 1) * (2*n + 1) / 6)
}
