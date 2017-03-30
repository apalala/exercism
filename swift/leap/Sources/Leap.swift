

class Year {
    let year: Int

    init(calendarYear: Int) {
       year = calendarYear
    }

    var isLeapYear: Bool {
        get {
            return year % 400 == 0 || year % 100 != 0 && year % 4 == 0
        }
    }
}