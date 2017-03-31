import Foundation

public func hey(_ input: String) -> String {
    let what = input.trimmingCharacters(in: CharacterSet.whitespacesAndNewlines)

    if what.isEmpty {
        return "Fine. Be that way!"
    }
    if what == what.uppercased() && hasLetter(what) {
        return "Whoa, chill out!"
    }
    if what.characters.last == "?" {
        return "Sure."
    }
    return "Whatever."
}

private func hasLetter(_ s: String) -> Bool {
    return s.unicodeScalars.reduce(false, {$0 || CharacterSet.letters.contains($1)})
}
