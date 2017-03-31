

func compute(_ a: String, against b: String) -> Int? {
    if a.characters.count != b.characters.count {
        return nil
    }

    var result = 0
    for (x, y) in zip(a.characters, b.characters) {
        if x != y {
            result += 1
        }
    }
    return result
}