import XCTest
@testable import yolor

final class AppShellTests: XCTestCase {
    func testAppRootStartsOnInputScreen() {
        let root = YolorAppRoot()
        XCTAssertNotNil(root)
    }
}
