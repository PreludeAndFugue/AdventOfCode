//
//  Problem07Tests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 08/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest


class Problem07Tests: XCTestCase {

    // MARK: - Part 1

    func test1() {
        let p = Problem07()
        let r = p.runComputers(memory: input1, phases: phases1)
        XCTAssertEqual(r, 43210)
    }


    func test2() {
        let p = Problem07()
        let r = p.runComputers(memory: input2, phases: phases2)
        XCTAssertEqual(r, 54321)
    }


    func test3() {
        let p = Problem07()
        let r = p.runComputers(memory: input3, phases: phases3)
        XCTAssertEqual(r, 65210)
    }


    // MARK: - Part 2

    func test4() {
        let p = Problem07()
        let r = p.runFeedbackComputers(memory: input4, phases: phases4)
        XCTAssertEqual(r, 139629729)
    }


    func test5() {
        let p = Problem07()
        let r = p.runFeedbackComputers(memory: input5, phases: phases5)
        XCTAssertEqual(r, 18216)
    }
}


// MARK: - Test data, part 1

private var input1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
private var phases1 = [4,3,2,1,0]

private var input2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
private var phases2 = [0,1,2,3,4]

private var input3 = [
    3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,
    31,99,0,0,0
]
private var phases3 = [1,0,4,3,2]


// MARK: - Test data, part 2

private var input4 = [
    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
]
private var phases4 = [9,8,7,6,5]

private var input5 = [
    3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,
    1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,
    0,0,10
]
private var phases5 = [9,7,8,5,6]
