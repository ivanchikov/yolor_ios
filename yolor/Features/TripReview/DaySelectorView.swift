import SwiftUI

struct DaySelectorView: View {
    let days: [DayDTO]
    let selectedDayIndex: Int
    let onSelect: (Int) -> Void

    var body: some View {
        HStack {
            ForEach(days, id: \.dayIndex) { day in
                Button(day.title) {
                    onSelect(day.dayIndex)
                }
                .buttonStyle(.borderedProminent)
                .tint(day.dayIndex == selectedDayIndex ? .blue : .gray)
            }
        }
    }
}

#Preview {
    DaySelectorView(days: TripDTO.preview.days, selectedDayIndex: 1, onSelect: { _ in })
}
