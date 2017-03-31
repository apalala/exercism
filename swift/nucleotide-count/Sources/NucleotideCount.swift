
let NUCLEOTIDES = "ACGT"

class DNA {
    let strand: String
    let _counts: [String: Int]?

    init?(strand: String) {
        self.strand = strand
        self._counts = DNA._do_count(strand)
        if self._counts == nil {
            return nil
        }
    }

    private static func _do_count(_ strand: String)-> [String: Int]? {
        var result: [String: Int] = [:]

        for c in NUCLEOTIDES.characters {
            result[String(c)] = 0
        }

        for c in strand.characters {
            let s = String(c)
            if let n = result[s] {
                result[s] = n + 1
            }
            else {
                return nil
            }
        }
        return result
    }

    func counts() -> [String: Int] {
        return self._counts!
    }


    func count(_ s:String) -> Int? {
        return counts()[s]
    }
}