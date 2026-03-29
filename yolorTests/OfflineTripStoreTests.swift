import Foundation
import XCTest
@testable import yolor

final class OfflineTripStoreTests: XCTestCase {
    func testSavingTripMakesItReadableOffline() throws {
        let directoryURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString, isDirectory: true)
        try FileManager.default.createDirectory(at: directoryURL, withIntermediateDirectories: true)
        let fileURL = directoryURL.appendingPathComponent("saved-trips.json")
        let store = OfflineTripStore(fileURL: fileURL)
        let trip = TripDTO.preview

        try store.save(trip)
        let saved = try store.loadAll()

        XCTAssertEqual(saved.first?.id, trip.id)
    }
}
