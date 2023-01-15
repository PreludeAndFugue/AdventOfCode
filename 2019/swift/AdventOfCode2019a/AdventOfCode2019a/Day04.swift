//
//  Day04.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation


func day04() {
    let range = 387638...919123

    let p1 = range.filter({ isValid(n: $0) }).count
    print(p1)

    let p2 = range.filter({ isValid(n: $0, exact: true) }).count
    print(p2)
}


func isValid(n: Int, exact: Bool = false) -> Bool {
    var n = n
    var currentM = 10
    var counts: [Int: Int] = [:]
    while n > 0 {
        let m = n % 10
        n /= 10

        if m > currentM {
            return false
        }

        counts[m, default: 0] += 1
        currentM = m
    }
    if exact {
        return counts.values.contains(2)
    } else {
        return counts.values.max()! > 1
    }
}
