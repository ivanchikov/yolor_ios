import SwiftUI

struct YolorAppRoot: View {
    @StateObject private var authViewModel = AuthViewModel()
    @State private var isShowingSavedTrips = false
    private let offlineTripStore = OfflineTripStore()

    var body: some View {
        NavigationStack {
            InputView()
                .sheet(isPresented: $isShowingSavedTrips) {
                    NavigationStack {
                        SavedTripsView(trips: (try? offlineTripStore.loadAll()) ?? [])
                    }
                }
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        ProfileMenuView(
                            authViewModel: authViewModel,
                            onShowSavedTrips: { isShowingSavedTrips = true }
                        )
                    }
                }
        }
    }
}
