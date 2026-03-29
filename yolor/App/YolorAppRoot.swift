import SwiftUI

struct YolorAppRoot: View {
    var body: some View {
        NavigationStack {
            InputView()
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        ProfileMenuView()
                    }
                }
        }
    }
}
