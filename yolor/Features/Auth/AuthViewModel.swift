import Combine
import Foundation

@MainActor
final class AuthViewModel: ObservableObject {
    @Published private(set) var session: UserSession?

    var isAuthenticated: Bool {
        session != nil
    }

    func signIn() {
        session = .preview
    }

    func signOut() {
        session = nil
    }
}
