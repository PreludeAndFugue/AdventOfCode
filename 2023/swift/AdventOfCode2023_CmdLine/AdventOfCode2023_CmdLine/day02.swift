//
//  day02.swift
//  AdventOfCode2023_CmdLine
//
//  Created by gary on 04/01/2024.
//

import Foundation

struct Day02 {
    func run() {
        let d = getInput("02")
        let games = parse(d: d)
        let red = 12
        let green = 13
        let blue = 14
        
        var part1 = 0
        var part2 = 0

        for (n, rounds) in games {
            var isValid = true
            var R = 0
            var G = 0
            var B = 0
            for round in rounds {
                let r = round["red", default: 0]
                let g = round["green", default: 0]
                let b = round["blue", default: 0]
                
                if r > red || g > green || b > blue {
                    isValid = false
                }
                R = max(R, r)
                G = max(G, g)
                B = max(B, b)
            }
            if isValid {
                part1 += n
            }
            part2 += R*G*B
        }
        print(part1)
        print(part2)
    }
}

private extension Day02 {
    func parse(d: String) -> [Int: [[String: Int]]] {
        var games: [Int: [[String: Int]]] = [:]
        for line in d.split(separator: "\n") {
            let parts = line.split(separator: ": ")
            let game = Int(parts[0].split(separator: " ")[1])!
            var rounds: [[String: Int]] = []
            for p1 in parts[1].split(separator: "; ") {
                var round: [String: Int] = [:]
                for p2 in p1.split(separator: ", ") {
                    let p3 = p2.split(separator: " ")
                    let colour = String(p3[1])
                    let n = Int(p3[0])
                    round[colour] = n
                }
                rounds.append(round)
            }
            games[game] = rounds
        }
        return games
    }
}
