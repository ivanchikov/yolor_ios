import Combine
import Foundation

@MainActor
final class GenerationViewModel: ObservableObject {
    @Published var progressMessage = "Generating trip..."
}
