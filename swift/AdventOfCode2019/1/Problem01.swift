//
//  Problem01.swift
//  AdventOfCode2019
//
//  Created by gary on 01/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

final class Problem01: Problem {
    private let file = "1/data01.txt"
    private lazy var masses = self.makeMasses()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 1, r1, r2)
    }
}


// MARK: - Private

private extension Problem01 {
    private func makeMasses() -> [Int] {
        let string = try! String(contentsOfFile: path + file)
        return string.makeIntegers(separator: "\n")
    }


    private func part1() -> Int {
        return masses.map(fuelForMass(_:)).sum()
    }


    private func part2() -> Int {
        return masses.map(fuelForMass2(_:)).sum()
    }


    private func fuelForMass(_ mass: Int) -> Int {
        Int(floor(Double(mass) / 3.0) - 2)
    }


    private func fuelForMass2(_ mass: Int) -> Int {
        var result: [Int] = []
        var addition = fuelForMass(mass)
        while addition > 0 {
            result.append(addition)
            addition = fuelForMass(addition)
        }
        return result.sum()
    }
}
