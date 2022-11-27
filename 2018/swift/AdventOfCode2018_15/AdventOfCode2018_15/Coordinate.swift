//
//  Coordinate.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation

struct Coordinate {
    let x: Int
    let y: Int
}


extension Coordinate {
    static let neighbours: [Coordinate] = [
        Coordinate(x: 0, y: -1),
        Coordinate(x: -1, y: 0),
        Coordinate(x: 1, y: 0),
        Coordinate(x: 0, y: 1)
    ]

    
    static func + (lhs: Coordinate, rhs: Coordinate) -> Coordinate {
        return Coordinate(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }
}


extension Coordinate: Hashable {}

extension Coordinate: CustomDebugStringConvertible {
    var debugDescription: String {
        return "(\(x), \(y))"
    }
}
