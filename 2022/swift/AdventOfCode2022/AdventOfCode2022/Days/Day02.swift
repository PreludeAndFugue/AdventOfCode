//
//  Day02.swift
//  AdventOfCode2022
//
//  Created by gary on 01/12/2022.
//

import Foundation

fileprivate let test1 = """
A Y
B X
C Z
"""

struct Day02: Day {
    let d = "02"

    let map: [String: Int] = [
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 0,
        "Y": 1,
        "Z": 2
    ]


    func run() throws -> (String, String) {
        let s = try getInput()
        var games: [(String, String)] = []
        for line in s.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n") {
            let parts = line.split(separator: " ")
            let p1 = String(parts[0])
            let p2 = String(parts[1])
            games.append((p1, p2))
        }
        return (part1(games: games), part2(games: games))
    }
}


// MARK: - Private

private extension Day02 {
    func part1(games: [(String, String)]) -> String {
        var totalScore = 0
        for (p1, p2) in games {
            totalScore += map[p2]! + 1
            switch map[p2]! - map[p1]! {
            case 1, -2:
                totalScore += 6
            case 0:
                totalScore += 3
            case -1, 2:
                totalScore += 0
            default:
                fatalError()
            }
        }
        return "\(totalScore)"
    }


    func part2(games: [(String, String)]) -> String {
        var totalScore = 0
        for (p1, result) in games {
            switch result {
            case "X":
                // lose
                totalScore += 0
                totalScore += (map[p1]! + 2) % 3 + 1
            case "Y":
                // draw
                totalScore += 3
                totalScore += map[p1]! + 1
            case "Z":
                // win
                totalScore += 6
                totalScore += (map[p1]! + 1) % 3 + 1
            default:
                fatalError()
            }
        }
        return "\(totalScore)"
    }
}
