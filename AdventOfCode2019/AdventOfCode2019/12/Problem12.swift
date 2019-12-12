//
//  Problem12.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem12: Problem {
    private let file = "12/data12.txt"

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 12, r1, r2)
    }
}


// MARK: - Private

private extension Problem12 {
    private func part1() -> Int {
        for c in [1, 2, 3, 4].combinations(r: 2) {
            print(c)
        }
        return 0
    }


    private func part2() -> Int {
        return 0
    }
}
