
class SumOfMultiples {
    static func toLimit(_ limit: Int, inMultiples:[Int]) -> Int {
        var multiples: Set<Int> = []
        for n in inMultiples.filter({$0 > 0}) {
            multiples.formUnion(stride(from: n, to:limit, by: n))
        }
        return multiples.reduce(0, +)
    }
}
