//
//  Day04.swift
//  AdventOfCode2022
//
//  Created by gary on 04/12/2022.
//

import Foundation

fileprivate let test1 = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

struct Day04: Day {
    let d = "04"

    func run() throws -> (String, String) {
        let s = try getInput()
        var data: [[ClosedRange<Int>]] = []
        for line in s.split(separator: "\n") {
            let rangeStrings = line.split(separator: ",")
            let ranges = rangeStrings.map({ makeRange(string: String($0)) })
            data.append(ranges)
        }
        let p1 = part1(ranges: data)
        return (p1, "")
    }
}


// MARK: - Private

private extension Day04 {
    func makeRange(string: String) -> ClosedRange<Int> {
        let bounds = string.split(separator: "-")
        let lower = Int(bounds[0])!
        let upper = Int(bounds[1])!
        return lower...upper
    }


    func part1(ranges: [[ClosedRange<Int>]]) -> String {
        var count = 0
        for pair in ranges {
            let p1 = pair[0]
            let p2 = pair[1]
            if p1.count <= p2.count {
                if p1.lowerBound >= p2.lowerBound && p1.upperBound <= p2.upperBound {
                    count += 1
                }
            } else {
                if p2.lowerBound >= p1.lowerBound && p2.upperBound <= p1.upperBound {
                    count += 1
                }
            }
        }
        return "\(count)"
    }
}
