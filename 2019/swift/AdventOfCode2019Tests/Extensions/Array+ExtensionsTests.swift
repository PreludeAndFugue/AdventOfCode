//
//  Array+ExtensionsTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 07/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class Array_ExtensionsTests: XCTestCase {
    func testPermutations() {
        XCTAssertEqual([[0, 1], [1, 0]], [0, 1].permutations())
    }


    func testPermutations1() {
        XCTAssertEqual([[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]], [0, 1, 2].permutations())
    }


    func testPermutations2() {
        XCTAssertEqual([["x", "y"], ["y", "x"]], ["x", "y"].permutations())
    }


    func testPermutations3() {
        XCTAssertEqual([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]], [0, 1, 2].permutations(r: 2))
    }


    func testPermutations4() {
        XCTAssertEqual([[0], [1], [2]], [0, 1, 2].permutations(r: 1))
    }


    func testPermutations5() {
        let perms = [0, 1, 2, 3].permutations()
        XCTAssertEqual(24, perms.count)
    }


    func testPermutations6() {
        let perms = [0, 1, 2, 3, 4].permutations()
        XCTAssertEqual(120, perms.count)
    }


    func testPermutations7() {
        XCTAssertEqual([], [0, 1, 2].permutations(r: 4))
    }
}
