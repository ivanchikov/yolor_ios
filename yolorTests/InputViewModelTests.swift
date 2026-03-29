import XCTest
@testable import yolor

@MainActor
final class InputViewModelTests: XCTestCase {
    func testSubmitRequiresDestinationOrURL() async throws {
        let viewModel = InputViewModel(apiClient: .preview)

        await viewModel.submitPrimaryInput("")

        XCTAssertEqual(viewModel.errorMessage, "Enter a destination or paste a supported social link.")
    }
}
