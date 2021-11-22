//
//  Coordinate.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

struct Coordinate {
    let x: Int
    let y: Int

    
    var isOrigin: Bool {
        return x == 0 && y == 0
    }


    var manhattanDistanceFromOrigin: Int {
        return abs(x) + abs(y)
    }


    var theta: Double {
        return atan2(Double(y), Double(x))
    }


    var length: Double {
        let w = Double(x)
        let z = Double(y)
        return sqrt(w * w + z * z)
    }


    func getGridNeighbours() -> [Coordinate] {
        return [
            self + Direction.left.vector,
            self + Direction.up.vector,
            self + Direction.right.vector,
            self + Direction.down.vector
        ]
    }

    
    static func + (lhs: Coordinate, rhs: Coordinate) -> Coordinate {
        return Coordinate(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }


    static func - (lhs: Coordinate, rhs: Coordinate) -> Coordinate {
        return Coordinate(x: lhs.x - rhs.x, y: lhs.y - rhs.y)
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
