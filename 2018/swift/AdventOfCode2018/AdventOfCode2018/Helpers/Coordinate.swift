//
//  Coordinate.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

struct Coordinate: Hashable {
    let x: Int
    let y: Int
}


// MARK: - Public API

extension Coordinate {
    func manhattanDistance(to other: Coordinate) -> Int {
        return abs(self.x - other.x) + abs(self.y - other.y)
    }


    func neighbours() -> [Coordinate] {
        var results: [Coordinate] = []
        for x in -1...1 {
            for y in -1...1 {
                if x == 0 && y == 0 { continue }
                let neighbour = Coordinate(x: self.x + x, y: self.y + y)
                results.append(neighbour)
            }
        }
        return results
    }
}


extension Coordinate: CustomDebugStringConvertible {
    var debugDescription: String {
        return "(\(x), \(y))"
    }
}
