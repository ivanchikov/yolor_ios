import Foundation

struct UserSession: Codable, Equatable {
    let userID: String
    let email: String

    static let preview = UserSession(
        userID: "user_preview",
        email: "traveler@yolor.app"
    )
}
