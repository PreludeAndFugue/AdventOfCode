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


    func turnRight() -> Direction {
        switch self {
        case .down:
            return .left
        case .left:
            return .up
        case .right:
            return .down
        case .up:
            return .right
        }
    }


    func turnLeft() -> Direction {
        switch self {
        case .down:
            return .right
        case .left:
            return .down
        case .right:
            return .up
        case .up:
            return .left
        }
    }
}
