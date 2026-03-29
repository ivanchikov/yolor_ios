import Foundation

struct TripDTO: Codable, Equatable {
    var id: String
    var days: [DayDTO]

    static let preview = TripDTO(
        id: "trip_preview",
        days: [
            DayDTO(dayIndex: 1, title: "Day 1"),
            DayDTO(dayIndex: 2, title: "Day 2"),
        ]
    )
}

struct DayDTO: Codable, Equatable {
    var dayIndex: Int
    var title: String
}
