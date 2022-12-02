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
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
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
            totalScore += map[p2]!
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
                totalScore += strategy(score: 0, player1: p1)
            case "Y":
                // draw
                totalScore += 3
                totalScore += strategy(score: 3, player1: p1)
            case "Z":
                // win
                totalScore += 6
                totalScore += strategy(score: 6, player1: p1)
            default:
                fatalError()
            }
        }
        return "\(totalScore)"
    }


    func strategy(score: Int, player1: String) -> Int {
        switch score {
        case 0:
            switch player1 {
            case "A":
                return map["C"]!
            case "B":
                return map["A"]!
            case "C":
                return map["B"]!
            default:
                fatalError()
            }
        case 3:
            return map[player1]!
        case 6:
            switch player1 {
            case "A":
                return map["B"]!
            case "B":
                return map["C"]!
            case "C":
                return map["A"]!
            default:
                fatalError()
            }
        default:
            fatalError()
        }
    }
}
