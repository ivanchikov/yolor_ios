import XCTest
@testable import yolor

final class TripReviewViewModelTests: XCTestCase {
    func testSelectingDayUpdatesSelectedDayIndex() async {
        let viewModel = await TripReviewViewModel(trip: .preview)

        await viewModel.selectDay(2)

        let selectedDayIndex = await viewModel.selectedDayIndex
        XCTAssertEqual(selectedDayIndex, 2)
    }
}
