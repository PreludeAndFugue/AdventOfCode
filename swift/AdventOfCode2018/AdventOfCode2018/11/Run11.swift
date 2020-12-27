//
//  Run11.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

let TEST_1: [(Int, Int, Int, Int)] = [
    (122, 79, 57, -5),
    (217, 196, 39, 0),
    (101, 153, 71, 4)
]

private let gridSerialNumber = 4842

func run11() {
    test11a()
    test11b()
    test11c()

    main11()
    main11a()
}


func main11() {
    var maxCoords: (Int, Int) = (0, 0)
    var maxPower = Int.min
    let cellPowers = makeCellPowers(serialNumber: gridSerialNumber)
    for x in 1...298 {
        for y in 1...298 {
            let cells = getGroup(x: x, y: y, size: 3)
            let power = groupPower(cells: cells, cellPowers: cellPowers)
            if power > maxPower {
                maxCoords = (x, y)
                maxPower = power
            }
        }
    }
    print(maxCoords, maxPower)
}


/*
 Note: need to cache power calculations for smaller grids.

 https://www.reddit.com/r/adventofcode/comments/a55c4a/optimisation_of_day11_especially_part_2/

 Current solution prints out local maximum at the end of each size. You can see that after
 size 10 the maximum doesn't change.
 */
func main11a() {
    var maxCoords: (Int, Int) = (0, 0)
    var maxPower = Int.min
    var maxSize = -1
    let cellPowers = makeCellPowers(serialNumber: gridSerialNumber)
    for d in 1...300 {
        print(d)
        for x in 1...(300 - d + 1) {
            for y in 1...(300 - d + 1) {
                let cells = getGroup(x: x, y: y, size: d)
                let power = groupPower(cells: cells, cellPowers: cellPowers)
                if power > maxPower {
                    maxCoords = (x, y)
                    maxPower = power
                    maxSize = d
                }
            }
        }
        print("end", d, maxCoords, maxPower, maxSize)
    }
    print(maxCoords, maxSize, maxPower)
}


// MARK: - Helpers

func getGroup(x: Int, y: Int, size: Int) -> [(Int, Int)] {
    var cells: [(Int, Int)] = []
    for dx in 0..<size {
        for dy in 0..<size {
            cells.append((x + dx, y + dy))
        }
    }
    return cells
}


func groupPower(cells: [(Int, Int)], cellPowers: [[Int]]) -> Int {
    var totalPower = 0
    for (x, y) in cells {
        totalPower += cellPowers[y - 1][x - 1]
    }
    return totalPower
}


func makeCellPowers(serialNumber: Int) -> [[Int]] {
    var results = Array(repeating: Array(repeating: 0, count: 300), count: 300)
    for x in 1...300 {
        for y in 1...300 {
            let cell = GridCell(x: x, y: y)
            results[y - 1][x - 1] = cell.power(serialNumber: serialNumber)
        }
    }
    return results
}
