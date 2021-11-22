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
        let image = Image(content: ["AB", "DC"])
        let sut = image.rotated(.R90)
        XCTAssertEqual(sut.content, ["DA", "CB"])
    }


    func testRotate180() {
        let image = Image(content: ["AB", "DC"])
        let sut1 = image.rotated(.R180)
        XCTAssertEqual(sut1.content, ["CD", "BA"])

        let sut2 = image.rotated(.R90).rotated(.R90)
        XCTAssertEqual(sut2.content, ["CD", "BA"])
    }


    func testRotate270() {
        let image = Image(content: ["AB", "DC"])
        let sut1 = image.rotated(.R270)
        XCTAssertEqual(sut1.content, ["BC", "AD"])

        let sut2 = image.rotated(.R90).rotated(.R90).rotated(.R90)
        XCTAssertEqual(sut2.content, ["BC", "AD"])
    }


    func testIdentity() {
        let image = Image(content: ["AB", "DC"])
        let sut1 = image.rotated(.R180).rotated(.R180)
        XCTAssertEqual(image.content, ["AB", "DC"])
        XCTAssertEqual(sut1.content, ["AB", "DC"])
    }


    func testFlip() {
        let image = Image(content: ["AB", "DC"])
        let sut = image.flipped()
        XCTAssertEqual(sut.content, ["DC", "AB"])
    }


    func testDoubleFlip() {
        let image = Image(content: ["AB", "DC"])
        let sut = image.flipped().flipped()
        XCTAssertEqual(sut.content, ["AB", "DC"])
    }
}
