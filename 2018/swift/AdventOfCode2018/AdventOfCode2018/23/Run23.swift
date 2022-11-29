//
//  Run23.swift
//  AdventOfCode2018
//
//  Created by gary on 28/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation

struct Coordinate3D: Equatable, Hashable, CustomDebugStringConvertible {
    let x: Int
    let y: Int
    let z: Int

    var debugDescription: String { "(\(x), \(y), \(z))" }

    func manhattanDistance(_ other: Coordinate3D) -> Int {
        abs(x - other.x) + abs(y - other.y) + abs(z - other.z)
    }
}

struct NanoBot: Equatable, Hashable, CustomDebugStringConvertible {
    let position: Coordinate3D
    let signalRadius: Int

    var debugDescription: String { "B(\(position), \(signalRadius))"}
}


func makeBots(string: String) -> [NanoBot] {
    var bots: [NanoBot] = []
    for line in string.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n") {
        let parts = line.split(separator: ",").map({ Int($0)! })
        let position = Coordinate3D(x: parts[0], y: parts[1], z: parts[2])
        let bot = NanoBot(position: position, signalRadius: parts[3])
        bots.append(bot)
    }
    return bots
}


func part1(bots: [NanoBot]) {
    let m = bots.max(by: { $0.signalRadius < $1.signalRadius })!
    var count = 0
    for b in bots {
        let d = m.position.manhattanDistance(b.position)
        if d <= m.signalRadius {
            count += 1
        }
    }
    print(count)
}


func part2(bots: [NanoBot]) {
    var distances: [NanoBot: Set<NanoBot>] = [:]
    for b1 in bots {
        distances[b1] = []
        for b2 in bots {
            if b2 == b1 { continue }
            if b1.position.manhattanDistance(b2.position) <= b1.signalRadius + b2.signalRadius {
                distances[b1, default: []].insert(b2)
            }
        }
    }

    let (bot, bots) = distances.max(by: { $0.value.count < $1.value.count })!
    print(bot)
    print(bots.count)

//    for (k, v) in distances {
//        print(k)
//        print(v)
//        print()
//    }
}


func run23() {
    let bots = makeBots(string: input23)
//    part1(bots: bots)
    part2(bots: bots)
}
