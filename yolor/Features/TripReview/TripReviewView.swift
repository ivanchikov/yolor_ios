import SwiftUI

struct TripReviewView: View {
    @StateObject private var viewModel = TripReviewViewModel(trip: .preview)

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            DaySelectorView(
                days: viewModel.trip.days,
                selectedDayIndex: viewModel.selectedDayIndex,
                onSelect: viewModel.selectDay
            )

            Text("Selected day: \(viewModel.selectedDayIndex)")

            EditToolbarView()
        }
        .padding()
    }
}

#Preview {
    TripReviewView()
}
