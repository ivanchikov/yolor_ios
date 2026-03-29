import Combine
import Foundation

@MainActor
final class TripReviewViewModel: ObservableObject {
    @Published private(set) var selectedDayIndex: Int
    let trip: TripDTO

    init(trip: TripDTO) {
        self.trip = trip
        self.selectedDayIndex = trip.days.first?.dayIndex ?? 1
    }

    func selectDay(_ dayIndex: Int) {
        selectedDayIndex = dayIndex
    }
}
