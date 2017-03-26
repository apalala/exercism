package triangle

import "math"

const testVersion = 3

func KindFromSides(a, b, c float64) Kind {
	if math.Min(a, math.Min(b, c)) <= 0 {
		return NaT
	}
	if 2*math.Max(a, math.Max(b, c)) > a+b+c {
		return NaT
	}
	if math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) {
		return NaT
	}
	if math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return NaT
	}

	var side_len = map[float64]int{}
	for _, side := range []float64{a, b, c} {
		_, ok := side_len[side]
		if ok {
			side_len[side] += 1
		} else {
			side_len[side] = 1
		}
	}

	n := len(side_len)
	switch n {
	case 1:
		return Equ
	case 2:
		return Iso
	default:
		return Sca
	}
}

type Kind byte

const (
	NaT Kind = iota // not a triangle
	Equ             // equilateral
	Iso             // isosceles
	Sca             // scalene
)
