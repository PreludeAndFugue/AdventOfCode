//
//  AscendingNumbersTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class AscendingNumbersTests: XCTestCase {
    func testNumbers_10_20() {
        let numbers = make(start: 10, count: 9)
        XCTAssertEqual(numbers, [11, 12, 13, 14, 15, 16, 17, 18, 19])
    }


    func testNumbers_88_111() {
        let numbers = make(start: 88, count: 4)
        XCTAssertEqual(numbers, [88, 89, 99, 111])
    }


    func testNumbers_99_114() {
        let numbers = make(start: 99, count: 5)
        XCTAssertEqual(numbers, [99, 111, 112, 113, 114])
    }


    func testNumbers_555_577() {
        let numbers = make(start: 555, count: 10)
        XCTAssertEqual(numbers, [555, 556, 557, 558, 559, 566, 567, 568, 569, 577])
    }


    func testIncrementSpeed() {
        measure {
            let _ = make(start: 555, count: 50_000)
        }
    }
}


private func make(start: Int, count: Int) -> [Int] {
    var numbers: [Int] = []
    let ascendingNumbers = AscendingNumbers(start: start)
    for _ in 0..<count {
        numbers.append(ascendingNumbers.next)
    }
    return numbers
}
