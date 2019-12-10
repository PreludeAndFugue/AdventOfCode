//
//  Coordinate.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

struct Coordinate {
    let x: Int
    let y: Int


    var manhattanDistanceFromOrigin: Int {
        return abs(x) + abs(y)
    }

    
    static func + (lhs: Coordinate, rhs: Coordinate) -> Coordinate {
        return Coordinate(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }


    static var origin: Coordinate {
        return Coordinate(x: 0, y: 0)
    }
}


extension Coordinate: Hashable {}


extension Coordinate: CustomDebugStringConvertible {
    var debugDescription: String {
        return "(\(x), \(y))"
    }
}
