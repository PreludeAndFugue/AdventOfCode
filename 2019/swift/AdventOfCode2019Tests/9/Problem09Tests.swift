//
//  Problem09Tests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 09/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class Problem09Tests: XCTestCase {
    func test1() {
        let console = AutoConsole(input: [])
        let computer = Computer(memory: input1, console: console, debug: false)
        computer.run()
        XCTAssertEqual(console.output, input1)
    }


    func test2() {
        let console = AutoConsole(input: [])
        let computer = Computer(memory: input2, console: console)
        computer.run()
        XCTAssertEqual(console.output.count, 1)
        XCTAssertEqual(console.output[0].base10Digits.count, 16)
    }


    func test3() {
        let console = AutoConsole(input: [])
        let computer = Computer(memory: input3, console: console)
        computer.run()
        XCTAssertEqual(console.output, output3)
    }


    func testOpcode203_1() {
        for i in 0...2000 {
            let console = AutoConsole(input: [i])
            let memory = [203, 3, 99]
            let computer = Computer(memory: memory, console: console)
            computer.run()
            XCTAssertEqual(computer.memory.asArray, [203, 3, 99, i])
        }
    }


    func testOpcode203_2() {
        for i in 0...2000 {
            let console = AutoConsole(input: [i])
            let memory = [203, 5, 99]
            let computer = Computer(memory: memory, console: console)
            computer.run()
            XCTAssertEqual(computer.memory.asArray, [203, 5, 99, 0, 0, i])
        }
    }


    func testOpcode203_3() {
        for i in 10...20 {
            let console = AutoConsole(input: [i])
            let memory = [109, 2, 203, 3, 99]
            let computer = Computer(memory: memory, console: console)
            computer.run()
            XCTAssertEqual(computer.memory.asArray, [109, 2, 203, 3, 99, i])
        }
    }
}


// MARK: - Test data

private let input1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
private let output1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

private let input2 = [1102,34915192,34915192,7,4,7,99,0]

private let input3 = [104,1125899906842624,99]
private let output3 = [1125899906842624]
