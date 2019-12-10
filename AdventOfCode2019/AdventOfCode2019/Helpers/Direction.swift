//
//  Direction.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

enum Direction {
    case up
    case down
    case left
    case right

    init(directionString: String) {
        switch directionString {
        case "U":
            self = .up
        case "D":
            self = .down
        case "L":
            self = .left
        case "R":
            self = .right
        default:
            fatalError()
        }
    }


    var vector: Coordinate {
        switch self {
        case .up:
            return Coordinate(x: 0, y: 1)
        case .down:
            return Coordinate(x: 0, y: -1)
        case .left:
            return Coordinate(x: -1, y: 0)
        case .right:
            return Coordinate(x: 1, y: 0)
        }
    }
}
