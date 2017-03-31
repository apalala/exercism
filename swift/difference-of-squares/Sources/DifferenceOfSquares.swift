

class Squares {
    let base: Int

    init(_ n: Int) {
        base = n
    }

    var squareOfSums: Int {
        let n = base
        let sum: Int = n * (n + 1) / 2
        return sum * sum
    }

    var sumOfSquares: Int {
        let n = base
        return n * (n + 1) * (2 * n + 1) / 6
    }

    var differenceOfSquares: Int {
        return squareOfSums - sumOfSquares
    }
}