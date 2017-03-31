

let RNA_MAP = [
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
]


class Nucleotide {
    let dna: String

    init(_ _dna: String) {
        dna = _dna
    }

    var complementOfDNA: String {
        let nucleotides: [String] = Array(dna.characters).map {RNA_MAP[String($0)]!}
        return nucleotides.joined()
    }
}