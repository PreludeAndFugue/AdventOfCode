//
//  ImageTests.swift
//  AdventOfCode2020Tests
//
//  Created by gary on 23/12/2020.
//

import XCTest
@testable import AdventOfCode2020

class ImageTests: XCTestCase {
    func testRotate90() throws {
        let image = Image(image: ["AB", "DC"])
        let sut = image.rotated(.R90)
        XCTAssertEqual(sut.content, ["DA", "CB"])
    }
}
