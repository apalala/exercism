import Foundation


let DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss"
let GIGASECOND = TimeInterval(1_000_000_000)


class Gigasecond {

    let futureDate : Date
    let formatter =  DateFormatter()

    init?(from: String) {
        formatter.dateFormat = DATE_FORMAT
        formatter.timeZone = TimeZone(secondsFromGMT: 0)

        guard let date = formatter.date(from: from) else {
            return nil
        }

        futureDate = Date(timeInterval: GIGASECOND, since: date)
    }

    var description: String {
        return formatter.string(from: futureDate)
    }
}
