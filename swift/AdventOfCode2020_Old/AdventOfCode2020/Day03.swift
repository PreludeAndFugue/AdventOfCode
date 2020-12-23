//
//  Day03.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

func day03() -> (Int, Int) {
    let map = String.lines(forDay: 3)
    let p1 = countTrees(map: map, col: 3, row: 1)

    let p2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        .map({ countTrees(map: map, col: $0.0, row: $0.1) })
        .product()

    return (p1, p2)
}


private func countTrees(map: [String], col: Int, row: Int) -> Int {
    let width = map[0].count
    var position = 0
    var treeCount = 0
    for (r, line) in map.enumerated() {
        if r % row != 0 { continue }
        let chr = line[line.index(line.startIndex, offsetBy: position)]
        if chr == "#" {
            treeCount += 1
        }
        position = (position + col) % width
    }
    return treeCount
}
