//
//  Tests11.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

// MARK: - Tests

func test11a() {
    for (x, y, serialNumber, powerTest) in TEST_1 {
        let gridCell = GridCell(x: x, y: y)
        let power = gridCell.power(serialNumber: serialNumber)
        assert(power == powerTest)
    }
}


func test11b() {
    let cellPowers = makeCellPowers(serialNumber: 18)
    let cells = getGroup(x: 33, y: 45, size: 3)
    let power = groupPower(cells: cells, cellPowers: cellPowers)
    assert(power == 29)
}


func test11c() {
    let cellPowers = makeCellPowers(serialNumber: 42)
    let cells = getGroup(x: 21, y: 61, size: 3)
    let power = groupPower(cells: cells, cellPowers: cellPowers)
    assert(power == 30)
}
