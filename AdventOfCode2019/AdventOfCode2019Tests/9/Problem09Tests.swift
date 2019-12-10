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
        let computer = Computer(memory: input1, console: console, debug: true)
        computer.run()
        print(console.output)
    }
}


// MARK: - Test data

private let input1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
private let output1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
