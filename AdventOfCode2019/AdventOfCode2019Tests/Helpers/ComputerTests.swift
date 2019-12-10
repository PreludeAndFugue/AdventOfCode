//
//  ComputerTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class ComputerTests: XCTestCase {
    func test01() {
        let input = [1, 0, 0, 0, 99]
        let output = [2, 0, 0, 0, 99]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]), debug: true)
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test02() {
        let input = [2, 3, 0, 3, 99]
        let output = [2, 3, 0, 6, 99]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]))
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test03() {
        let input = [2,4,4,5,99,0]
        let output = [2,4,4,5,99,9801]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]))
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test04() {
        let input = [1,1,1,4,99,5,6,0,99]
        let output = [30,1,1,4,2,5,6,0,99]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]))
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test05() {
        let input = [1002,4,3,4,33]
        let output = [1002,4,3,4,99]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]))
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test06() {
        let input = [1101,100,-1,4,0]
        let output = [1101,100,-1,4,99]
        let computer = Computer(memory: input, console: AutoConsole(input: [0]))
        computer.run()
        XCTAssertEqual(output, computer.memory.asArray)
    }


    func test07() {
        let input = [3,0,4,0,99]
        for i in 1...20 {
            let output = [i]
            let console = AutoConsole(input: [i])
            let computer = Computer(memory: input, console: console)
            computer.run()
            XCTAssertEqual(output, console.output)
        }
    }


    func test08() {
        let input = [3,9,8,9,10,9,4,9,99,-1,8]
        let console = AutoConsole(input: [8])
        let computer = Computer(memory: input, console: console, debug: true)
        computer.run()
        XCTAssertEqual([1], console.output)
    }


    func test09() {
        let input = [3,9,8,9,10,9,4,9,99,-1,8]
        for n in [1, 2, 3, 4, 5, 6, 7, 9, 10, 11] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([0], console.output)
        }
    }


    func test10() {
        let input = [3,9,7,9,10,9,4,9,99,-1,8]
        for n in [1, 2, 3, 4, 5, 6, 7] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([1], console.output)
        }
    }


    func test11() {
        let input = [3,9,7,9,10,9,4,9,99,-1,8]
        for n in [8, 9, 10, 11, 12, 30] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([0], console.output)
        }
    }


    func test12() {
        let input = [3,3,1108,-1,8,3,4,3,99]
        let console = AutoConsole(input: [8])
        let computer = Computer(memory: input, console: console, debug: true)
        computer.run()
        XCTAssertEqual([1], console.output)
    }


    func test13() {
        let input = [3,3,1108,-1,8,3,4,3,99]
        for n in [1, 2, 3, 4, 5, 6, 7, 9, 10, 11] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([0], console.output)
        }
    }


    func test14() {
        let input = [3,3,1107,-1,8,3,4,3,99]
        for n in [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([1], console.output)
        }
    }


    func test15() {
        let input = [3,3,1107,-1,8,3,4,3,99]
        for n in [8, 9, 10, 11, 12, 30] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console, debug: true)
            computer.run()
            XCTAssertEqual([0], console.output)
        }
    }


    func test16() {
        let input = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        let console = AutoConsole(input: [0])
        let computer = Computer(memory: input, console: console)
        computer.run()
        XCTAssertEqual([0], console.output)
    }


    func test17() {
        let input = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        for n in [-10, -5, -4, -1, 1, 4, 5, 10] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console)
            computer.run()
            XCTAssertEqual([1], console.output)
        }
    }


    func test18() {
        let input = [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,
            125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
        let console = AutoConsole(input: [8])
        let computer = Computer(memory: input, console: console)
        computer.run()
        XCTAssertEqual([1000], console.output)
    }


    func test19() {
        let input = [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,
            125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
        for n in [-10, -5, -1, 0, 1, 2, 6, 7] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console)
            computer.run()
            XCTAssertEqual([999], console.output)
        }
    }


    func test20() {
        let input = [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,
            125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
        for n in [9, 10, 15, 20, 100] {
            let console = AutoConsole(input: [n])
            let computer = Computer(memory: input, console: console)
            computer.run()
            XCTAssertEqual([1001], console.output)
        }
    }
}
