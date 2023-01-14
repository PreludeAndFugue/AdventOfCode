//
//  Int+ExtensionsTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class Int_ExtensionsTests: XCTestCase {
    func testBase10Digits_123() {
        let n = 123
        XCTAssertEqual(n.base10Digits, [1, 2, 3])
    }


    func testBase10Digits_0() {
        let n = 0
        XCTAssertEqual(n.base10Digits, [0])
    }


    func testBase10Digits_1() {
        let n = 1
        XCTAssertEqual(n.base10Digits, [1])
    }


    func testBase10Digits_7() {
        let n = 7
        XCTAssertEqual(n.base10Digits, [7])
    }


    func testBase10Digits_10() {
        let n = 10
        XCTAssertEqual(n.base10Digits, [1, 0])
    }


    func testBase10Digits_45() {
        let n = 45
        XCTAssertEqual(n.base10Digits, [4, 5])
    }


    func testBase10Digits_100() {
        let n = 100
        XCTAssertEqual(n.base10Digits, [1, 0, 0])
    }


    func testFromDigits_1() {
        let digits = [1]
        XCTAssertEqual(Int(fromDigits: digits), 1)
    }


    func testFromDigits_34() {
        let digits = [3, 4]
        XCTAssertEqual(Int(fromDigits: digits), 34)
    }


    func testFromDigits_10030() {
        let digits = [1, 0, 0, 3, 0]
        XCTAssertEqual(Int(fromDigits: digits), 10030)
    }


    func testModularPower1() {
        XCTAssertEqual(modularPower(base: 4, exponent: 13, modulus: 497), 445)
        XCTAssertEqual(modularPower(base: 2, exponent: 5, modulus: 13), 6)
    }
}
