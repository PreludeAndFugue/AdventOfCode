//
//  TileTests.swift
//  AdventOfCode2020Tests
//
//  Created by gary on 24/12/2020.
//

import XCTest
@testable import AdventOfCode2020

class TileTests: XCTestCase {
    func testEdges() {
        let tile = Tile(n: 1, image: ["AB", "DC"])
        XCTAssertEqual(tile.topEdge, Tile.Edge.top("AB"))
        XCTAssertEqual(tile.rightEdge, Tile.Edge.right("BC"))
        XCTAssertEqual(tile.bottomEdge, Tile.Edge.bottom("DC"))
        XCTAssertEqual(tile.leftEdge, Tile.Edge.left("AD"))
    }


    func testNoMatchingEdges() {
        let t1 = Tile(n: 1, image: ["AB", "CD"])
        let t2 = Tile(n: 2, image: ["EF", "GH"])
        let match = t1.hasMatchingEdges(with: t2)
        XCTAssertNil(match)
    }


    func testMatchingEdges1() {
        let t1 = Tile(n: 1, image: ["AB", "DC"])
        let t2 = Tile(n: 2, image: ["EF", "AB"])
        let match = t1.hasMatchingEdges(with: t2)
        XCTAssertNotNil(match)
        XCTAssertEqual(match?.0, Tile.Edge.top("AB"))
        XCTAssertEqual(match?.1, Tile.Edge.bottom("AB"))
    }
}
