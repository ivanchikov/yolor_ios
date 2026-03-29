import Foundation

struct OfflineTripStore {
    let fileManager: FileManager
    let fileURL: URL

    init(fileManager: FileManager = .default, fileURL: URL? = nil) {
        self.fileManager = fileManager
        self.fileURL = fileURL ?? fileManager.temporaryDirectory.appendingPathComponent("saved-trips.json")
    }

    func save(_ trip: TripDTO) throws {
        let existingTrips = (try? loadAll()) ?? []
        let updatedTrips = existingTrips.filter { $0.id != trip.id } + [trip]
        let data = try JSONEncoder().encode(updatedTrips)

        try data.write(to: fileURL, options: .atomic)
    }

    func loadAll() throws -> [TripDTO] {
        guard fileManager.fileExists(atPath: fileURL.path) else {
            return []
        }

        let data = try Data(contentsOf: fileURL)
        return try JSONDecoder().decode([TripDTO].self, from: data)
    }
}
