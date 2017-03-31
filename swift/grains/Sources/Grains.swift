import Darwin

enum GrainsError: Error {
    case inputTooHigh(message: String)
    case inputTooLow(message: String)
}


private func pow2(_ n: Int) -> Double {
    return Double(pow(2.0, Double(n)))
}

func square(_ n:Int) throws -> Double {
    if n < 1 {
        throw GrainsError.inputTooLow(
                message:"Input[\(n)] invalid. Input should be between 1 and 64 (inclusive)"
        )
    }
    if n > 64 {
        throw GrainsError.inputTooHigh(
                message:"Input[\(n)] invalid. Input should be between 1 and 64 (inclusive)"
        )
    }
    return pow2(n-1)
}


var total: Double {
    return pow2(64)
}
