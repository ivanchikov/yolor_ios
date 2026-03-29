import SwiftUI

struct InputView: View {
    @StateObject private var viewModel = InputViewModel(apiClient: .preview)

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            TextField("Where to?", text: $viewModel.primaryInput)
                .textFieldStyle(.roundedBorder)

            Button("Start Planning") {
                Task {
                    await viewModel.submitPrimaryInput(viewModel.primaryInput)
                }
            }

            if let errorMessage = viewModel.errorMessage {
                Text(errorMessage)
                    .foregroundStyle(.red)
                    .font(.footnote)
            }
        }
        .padding()
        .navigationTitle("Yolor")
    }
}

#Preview {
    InputView()
}
