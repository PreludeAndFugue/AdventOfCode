//
//  Coordinate.swift
//  AdventOfCode2020
//
//  Created by gary on 24/12/2020.
//

import Foundation

struct Coordinate {
    let x: Int
    let y: Int
}


extension Coordinate {
    static func + (lhs: Coordinate, rhs: Coordinate) -> Coordinate {
        Coordinate(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }
}


// MARK: - Hashable

extension Coordinate: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(x)
        hasher.combine(y)
    }
}


// MARK: - CustomDebugStringConvertible

extension Coordinate: CustomDebugStringConvertible {
    var debugDescription: String {
        "(\(self.x), \(self.y))"
    }
}
