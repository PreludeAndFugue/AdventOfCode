//
//  Computer+OpcodeTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 07/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest

class Computer_OpcodeTests: XCTestCase {
    func testFinish() {
        let opcodeData = Computer.OpcodeData(99)
        XCTAssertEqual(opcodeData.opcode, .finish)
    }
}
