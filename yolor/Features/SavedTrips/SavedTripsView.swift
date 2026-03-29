import SwiftUI

struct SavedTripsView: View {
    let trips: [TripDTO]

    var body: some View {
        List(trips, id: \.id) { trip in
            VStack(alignment: .leading, spacing: 4) {
                Text("Trip \(trip.id)")
                    .font(.headline)
                Text("\(trip.days.count) days available offline")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .navigationTitle("Saved Trips")
    }
}

#Preview {
    NavigationStack {
        SavedTripsView(trips: [.preview])
    }
}
