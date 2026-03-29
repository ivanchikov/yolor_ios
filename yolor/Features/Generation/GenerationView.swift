import SwiftUI

struct GenerationView: View {
    @StateObject private var viewModel = GenerationViewModel()

    var body: some View {
        ProgressView(viewModel.progressMessage)
    }
}

#Preview {
    GenerationView()
}
