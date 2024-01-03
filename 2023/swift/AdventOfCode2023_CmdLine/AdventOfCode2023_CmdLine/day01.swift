//
//  day01.swift
//  AdventOfCode2023_CmdLine
//
//  Created by gary on 03/01/2024.
//

import Foundation

let d = getInput("01")

struct Day01 {
    func run() {
        let d = getInput("01")

        let (p1, p2) = parts(d: d)
        print(p1)
        print(p2)
    }
}

private extension Day01 {
    func parts(d: String) -> (Int, Int) {
        let nums: [String: Character] = [
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        ]
        var numsReversed: [String: Character] = [:]
        for num in nums.keys {
            numsReversed[String(num.reversed())] = nums[num]
        }


        var result1: [Int] = []
        var result2: [Int] = []
        for line in d.split(separator: "\n") {
            var chars1: [Character] = []
            var chars2: [Character] = []

            chars1.append(findFirst(in: line, nums: [:], isPart2: false))
            chars2.append(findFirst(in: line, nums: nums, isPart2: true))

            let lineReversed = Substring(line.reversed())
            chars1.append(findFirst(in: lineReversed, nums: [:], isPart2: false))
            chars2.append(findFirst(in: lineReversed, nums: numsReversed, isPart2: true))

            let n1 = chars1.map({ String($0) }).joined()
            result1.append(Int(n1)!)

            let n2 = chars2.map({ String($0) }).joined()
            result2.append(Int(n2)!)
        }
        return (result1.reduce(0, +), result2.reduce(0, +))
    }


    func findFirst(in line: Substring, nums: [String: Character], isPart2: Bool = false) -> Character {
        for (i, ch) in line.enumerated() {
            if ch.isNumber {
                return ch
            }
            if isPart2 {
                for num in nums.keys {
                    if line[line.index(line.startIndex, offsetBy: i)...].starts(with: num) {
                        return nums[num]!
                    }
                }
            }
        }
        // Should never be here.
        return "0"
    }
}
