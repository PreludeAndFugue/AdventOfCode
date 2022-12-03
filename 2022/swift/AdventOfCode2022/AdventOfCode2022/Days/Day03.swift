//
//  Day03.swift
//  AdventOfCode2022
//
//  Created by gary on 02/12/2022.
//

import Foundation

struct Day03: Day {
    static let lowercase = "abcdefghijklmnopqrstuvwxyz"
    static let uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    private let test1 = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

    let d = "03"
    let priority: [Character: Int]


    init() {
        var p: [Character: Int] = [:]
        for (i, c) in Self.lowercase.enumerated() {
            p[c] = i + 1
            p[c.uppercased().first!] = i + 27
        }
        priority = p
    }


    func run() throws -> (String, String) {
        let s = try getInput()
        let parts = s.trimmingCharacters(in: .whitespacesAndNewlines)
            .split(separator: "\n")
            .map({ String($0) })
        return (part1(parts: parts), part2(parts: parts))
    }
}


private extension Day03 {
    func part1(parts: [String]) -> String {
        var prioritySum = 0
        for part in parts {
            let l = part.count
            assert(l % 2 == 0)
            let m = l / 2
            let middle = part.index(part.startIndex, offsetBy: m)
            let p1 = Set(part[..<middle])
            let p2 = Set(part[middle...])
            let i = p1.intersection(p2)
            assert(i.count == 1)
            prioritySum += priority[i.first!]!
        }
        return "\(prioritySum)"
    }


    func part2(parts: [String]) -> String {
        var prioritySum = 0
        assert(parts.count % 3 == 0)
        var all: Set<Character> = []
        for (i, part) in parts.enumerated() {
            switch i % 3 {
            case 0:
                all = Set(part)
            case 1:
                all = all.intersection(Set(part))
            case 2:
                all = all.intersection(Set(part))
                assert(all.count == 1)
                prioritySum += priority[all.first!]!
            default:
                break
            }
        }
        return "\(prioritySum)"
    }
}
