//
//  Problem04.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem04: Problem {
    private let start = 387638
    private let stop = 919123

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(r1, r2)
    }
}


// MARK: - Private

private extension Problem04 {
    private func part1() -> Int {
        var count = 0
        let ascendingNumbers = AscendingNumbers(start: start)
        while true {
            let n = ascendingNumbers.next
            if n > stop { break }
            if hasDoubleDigit(n) {
                count += 1
            }
        }
        return count
    }


    private func part2() -> Int {
        var count = 0
        let ascendingNumbers = AscendingNumbers(start: start)
        while true {
            let n = ascendingNumbers.next
            if n > stop { break }
            if hasExactDoubleDigit(n) {
                count += 1
            }
        }
        return count
    }


    private func hasDoubleDigit(_ n: Int) -> Bool {
        let digits = n.base10Digits
        for (m, n) in zip(digits.dropLast(), digits.dropFirst()) {
            if m == n {
                return true
            }
        }
        return false
    }


    private func hasExactDoubleDigit(_ n: Int) -> Bool {
        var counter: [Int: Int] = [:]
        for digit in n.base10Digits {
            counter[digit, default: 0] += 1
        }
        return Array(counter.values).contains(2)
    }
}
