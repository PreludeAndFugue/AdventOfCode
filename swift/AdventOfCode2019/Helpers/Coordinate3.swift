//
//  Coordinate3.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

struct Coordinate3 {
    let x: Int
    let y: Int
    let z: Int
}


extension Coordinate3 {
    static func + (lhs: Coordinate3, rhs: Coordinate3) -> Coordinate3 {
        return Coordinate3(x: lhs.x + rhs.x, y: lhs.y + rhs.y, z: lhs.z + rhs.z)
    }


    static func - (lhs: Coordinate3, rhs: Coordinate3) -> Coordinate3 {
        return Coordinate3(x: lhs.x - rhs.x, y: lhs.y - rhs.y, z: lhs.z - rhs.z)
    }


    static func += (lhs: inout Coordinate3, rhs: Coordinate3) {
        lhs = lhs + rhs
    }


    static func -= (lhs: inout Coordinate3, rhs: Coordinate3) {
        lhs = lhs - rhs
    }


    static prefix func - (coordinate: Coordinate3) -> Coordinate3 {
        return Coordinate3(x: -coordinate.x, y: -coordinate.y, z: -coordinate.z)
    }


    static var origin: Coordinate3 {
        return Coordinate3(x: 0, y: 0, z: 0)
    }
}



extension Coordinate3: CustomDebugStringConvertible {
    var debugDescription: String {
        return "\(x), \(y), \(z)"
    }
}
