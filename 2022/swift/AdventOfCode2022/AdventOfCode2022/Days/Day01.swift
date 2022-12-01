//
//  Day01.swift
//  AdventOfCode2022
//
//  Created by gary on 26/11/2022.
//

import Foundation


struct Day01: Day {
    let d = "01"


    func run() throws -> (String, String) {
        let s = try getInput()
        var all: [[Int]] = []
        var current: [Int] = []
        for line in s.trimmingCharacters(in: .whitespaces).split(separator: "\n", omittingEmptySubsequences: false) {
            if line.isEmpty {
                all.append(current)
                current = []
            } else {
                let n = Int(line)!
                current.append(n)
            }
        }
        if !current.isEmpty {
            all.append(current)
        }
        let ns = all.map({ $0.reduce(0, +) }).sorted()
        return (part1(input: ns), part2(input: ns))
    }
}


// MARK: - Private

private extension Day01 {
    func part1(input: [Int]) -> String {
        let n = input.last!
        return "\(n)"
    }


    func part2(input: [Int]) -> String {
        let start = input.index(input.endIndex, offsetBy: -3)
        let end = input.endIndex
        let m = input[start..<end].reduce(0, +)
        return "\(m)"
    }
}
