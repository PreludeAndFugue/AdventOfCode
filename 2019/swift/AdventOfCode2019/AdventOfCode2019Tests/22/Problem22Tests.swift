//
//  Problem22Tests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 27/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest
@testable import AdventOfCode2019

class Problem22Tests: XCTestCase {
    func test1() {
        let cards = Array(0...9)
        let p = Problem22()
        XCTAssertEqual(p.dealIntoNewStack(cards: cards), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        XCTAssertEqual(p.dealIntoNewStack(cards: p.dealIntoNewStack(cards: cards)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        XCTAssertEqual(p.cut(n: 3, cards: cards), [3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
        XCTAssertEqual(p.cut(n: -4, cards: cards), [6, 7, 8, 9, 0, 1, 2, 3, 4, 5])

        XCTAssertEqual(p.deal(n: 3, cards: cards), [0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
    }


    func test2() {
        let cards = Array(0...9)
        let p = Problem22()
        let result = p.dealIntoNewStack(cards: p.dealIntoNewStack(cards: p.deal(n: 7, cards: cards)))
        XCTAssertEqual(result, [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
    }


    func test3() {
        let cards = Array(0...9)
        let p = Problem22()
        let result = p.dealIntoNewStack(cards: p.deal(n: 7, cards: p.cut(n: 6, cards: cards)))
        XCTAssertEqual(result, [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])
    }


    func test4() {
        let cards = Array(0...9)
        let p = Problem22()
        let result = p.cut(n: -2, cards: p.deal(n: 9, cards: p.deal(n: 7, cards: cards)))
        XCTAssertEqual(result, [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])
    }


    func test5() {
        let cards = Array(0...9)
        let p = Problem22()
        var result = p.dealIntoNewStack(cards: cards)
        result = p.cut(n: -2, cards: result)
        result = p.deal(n: 7, cards: result)
        result = p.cut(n: 8, cards: result)
        result = p.cut(n: -4, cards: result)
        result = p.deal(n: 7, cards: result)
        result = p.cut(n: 3, cards: result)
        result = p.deal(n: 9, cards: result)
        result = p.deal(n: 3, cards: result)
        result = p.cut(n: -1, cards: result)
        XCTAssertEqual(result, [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
    }


    func test6() {
        let p = Problem22()
        XCTAssertEqual(p.dealIntoNewStack(i: 0, count: 10), 9)
        XCTAssertEqual(p.dealIntoNewStack(i: 1, count: 10), 8)
        XCTAssertEqual(p.dealIntoNewStack(i: 2, count: 10), 7)
        XCTAssertEqual(p.dealIntoNewStack(i: 3, count: 10), 6)
        XCTAssertEqual(p.dealIntoNewStack(i: 4, count: 10), 5)
        XCTAssertEqual(p.dealIntoNewStack(i: 5, count: 10), 4)
        XCTAssertEqual(p.dealIntoNewStack(i: 6, count: 10), 3)
        XCTAssertEqual(p.dealIntoNewStack(i: 7, count: 10), 2)
        XCTAssertEqual(p.dealIntoNewStack(i: 8, count: 10), 1)
        XCTAssertEqual(p.dealIntoNewStack(i: 9, count: 10), 0)
    }


    func test7() {
        let p = Problem22()
        XCTAssertEqual(p.cut(i: 0, n: 3, count: 10), 7)
        XCTAssertEqual(p.cut(i: 1, n: 3, count: 10), 8)
        XCTAssertEqual(p.cut(i: 2, n: 3, count: 10), 9)
        XCTAssertEqual(p.cut(i: 3, n: 3, count: 10), 0)
        XCTAssertEqual(p.cut(i: 4, n: 3, count: 10), 1)
        XCTAssertEqual(p.cut(i: 5, n: 3, count: 10), 2)
        XCTAssertEqual(p.cut(i: 6, n: 3, count: 10), 3)
        XCTAssertEqual(p.cut(i: 7, n: 3, count: 10), 4)
        XCTAssertEqual(p.cut(i: 8, n: 3, count: 10), 5)
        XCTAssertEqual(p.cut(i: 9, n: 3, count: 10), 6)
    }


    func test8() {
        let p = Problem22()
        XCTAssertEqual(p.cut(i: 0, n: -4, count: 10), 4)
        XCTAssertEqual(p.cut(i: 1, n: -4, count: 10), 5)
        XCTAssertEqual(p.cut(i: 2, n: -4, count: 10), 6)
        XCTAssertEqual(p.cut(i: 3, n: -4, count: 10), 7)
        XCTAssertEqual(p.cut(i: 4, n: -4, count: 10), 8)
        XCTAssertEqual(p.cut(i: 5, n: -4, count: 10), 9)
        XCTAssertEqual(p.cut(i: 6, n: -4, count: 10), 0)
        XCTAssertEqual(p.cut(i: 7, n: -4, count: 10), 1)
        XCTAssertEqual(p.cut(i: 8, n: -4, count: 10), 2)
        XCTAssertEqual(p.cut(i: 9, n: -4, count: 10), 3)
    }


    func test9() {
        let p = Problem22()
        XCTAssertEqual(p.deal(i: 0, n: 3, count: 10), 0)
        XCTAssertEqual(p.deal(i: 1, n: 3, count: 10), 3)
        XCTAssertEqual(p.deal(i: 2, n: 3, count: 10), 6)
        XCTAssertEqual(p.deal(i: 3, n: 3, count: 10), 9)
        XCTAssertEqual(p.deal(i: 4, n: 3, count: 10), 2)
        XCTAssertEqual(p.deal(i: 5, n: 3, count: 10), 5)
        XCTAssertEqual(p.deal(i: 6, n: 3, count: 10), 8)
        XCTAssertEqual(p.deal(i: 7, n: 3, count: 10), 1)
        XCTAssertEqual(p.deal(i: 8, n: 3, count: 10), 4)
        XCTAssertEqual(p.deal(i: 9, n: 3, count: 10), 7)
    }


    func test10() {
        func t(i: Int, count: Int) -> Int {
            var i = i
            let p = Problem22()
            i = p.deal(i: i, n: 7, count: count)
            i = p.dealIntoNewStack(i: i, count: count)
            i = p.dealIntoNewStack(i: i, count: count)
            return i
        }
        XCTAssertEqual(t(i: 0, count: 10), 0)
        XCTAssertEqual(t(i: 1, count: 10), 7)
        XCTAssertEqual(t(i: 2, count: 10), 4)
        XCTAssertEqual(t(i: 3, count: 10), 1)
        XCTAssertEqual(t(i: 4, count: 10), 8)
        XCTAssertEqual(t(i: 5, count: 10), 5)
        XCTAssertEqual(t(i: 6, count: 10), 2)
        XCTAssertEqual(t(i: 7, count: 10), 9)
        XCTAssertEqual(t(i: 8, count: 10), 6)
        XCTAssertEqual(t(i: 9, count: 10), 3)
    }


    func test11() {
        func t(i: Int, count: Int) -> Int {
            var i = i
            let p = Problem22()
            i = p.cut(i: i, n: 6, count: count)
            i = p.deal(i: i, n: 7, count: count)
            i = p.dealIntoNewStack(i: i, count: count)
            return i
        }
        XCTAssertEqual(t(i: 0, count: 10), 1)
        XCTAssertEqual(t(i: 1, count: 10), 4)
        XCTAssertEqual(t(i: 2, count: 10), 7)
        XCTAssertEqual(t(i: 3, count: 10), 0)
        XCTAssertEqual(t(i: 4, count: 10), 3)
        XCTAssertEqual(t(i: 5, count: 10), 6)
        XCTAssertEqual(t(i: 6, count: 10), 9)
        XCTAssertEqual(t(i: 7, count: 10), 2)
        XCTAssertEqual(t(i: 8, count: 10), 5)
        XCTAssertEqual(t(i: 9, count: 10), 8)
    }


    func test12() {
        func t(i: Int, count: Int) -> Int {
            var i = i
            let p = Problem22()
            i = p.deal(i: i, n: 7, count: count)
            i = p.deal(i: i, n: 9, count: count)
            i = p.cut(i: i, n: -2, count: count)
            return i
        }
        XCTAssertEqual(t(i: 0, count: 10), 2)
        XCTAssertEqual(t(i: 1, count: 10), 5)
        XCTAssertEqual(t(i: 2, count: 10), 8)
        XCTAssertEqual(t(i: 3, count: 10), 1)
        XCTAssertEqual(t(i: 4, count: 10), 4)
        XCTAssertEqual(t(i: 5, count: 10), 7)
        XCTAssertEqual(t(i: 6, count: 10), 0)
        XCTAssertEqual(t(i: 7, count: 10), 3)
        XCTAssertEqual(t(i: 8, count: 10), 6)
        XCTAssertEqual(t(i: 9, count: 10), 9)
    }


    func test13() {
        func t(i: Int, count: Int) -> Int {
            var i = i
            let p = Problem22()
            i = p.dealIntoNewStack(i: i, count: count)
            i = p.cut(i: i, n: -2, count: count)
            i = p.deal(i: i, n: 7, count: count)
            i = p.cut(i: i, n: 8, count: count)
            i = p.cut(i: i, n: -4, count: count)
            i = p.deal(i: i, n: 7, count: count)
            i = p.cut(i: i, n: 3, count: count)
            i = p.deal(i: i, n: 9, count: count)
            i = p.deal(i: i, n: 3, count: count)
            i = p.cut(i: i, n: -1, count: count)
            return i
        }
        XCTAssertEqual(t(i: 0, count: 10), 7)
        XCTAssertEqual(t(i: 1, count: 10), 4)
        XCTAssertEqual(t(i: 2, count: 10), 1)
        XCTAssertEqual(t(i: 3, count: 10), 8)
        XCTAssertEqual(t(i: 4, count: 10), 5)
        XCTAssertEqual(t(i: 5, count: 10), 2)
        XCTAssertEqual(t(i: 6, count: 10), 9)
        XCTAssertEqual(t(i: 7, count: 10), 6)
        XCTAssertEqual(t(i: 8, count: 10), 3)
        XCTAssertEqual(t(i: 9, count: 10), 0)
    }
}
