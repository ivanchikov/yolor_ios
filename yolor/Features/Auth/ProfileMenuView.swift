import SwiftUI

struct ProfileMenuView: View {
    @ObservedObject var authViewModel: AuthViewModel
    let onShowSavedTrips: () -> Void

    var body: some View {
        Menu {
            if authViewModel.isAuthenticated {
                Button("Saved Trips", action: onShowSavedTrips)
                Button("Sign Out", action: authViewModel.signOut)
            } else {
                Button("Sign In", action: authViewModel.signIn)
            }
        } label: {
            Label("Profile", systemImage: "person.crop.circle")
        }
    }
}

#Preview {
    ProfileMenuView(
        authViewModel: AuthViewModel(),
        onShowSavedTrips: {}
    )
}
