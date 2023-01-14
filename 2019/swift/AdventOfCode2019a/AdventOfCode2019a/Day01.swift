//
//  Day01.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation


func day01() {
    let ns = getInts(file: "01")

    let p1 = ns.map({ $0 / 3 - 2 }).reduce(0, +)
    print(p1)

    let p2 = ns.map({ part2a(n: $0) }).reduce(0, +)
    print(p2)
}


private func part2a(n: Int) -> Int {
    let m = (n / 3) - 2
    if m > 0 {
        return m + part2a(n: m)
    } else {
        return 0
    }
}
