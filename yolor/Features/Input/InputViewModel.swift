import Combine
import Foundation

@MainActor
final class InputViewModel: ObservableObject {
    @Published var primaryInput = ""
    @Published var errorMessage: String?

    let apiClient: APIClient

    init(apiClient: APIClient) {
        self.apiClient = apiClient
    }

    func submitPrimaryInput(_ value: String) async {
        guard value.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty == false else {
            errorMessage = "Enter a destination or paste a supported social link."
            return
        }

        errorMessage = nil
    }
}
