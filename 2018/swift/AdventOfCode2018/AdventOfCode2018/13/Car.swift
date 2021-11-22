//
//  Car.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Car {
    enum Direction: Character {
        case up = "^"
        case down = "v"
        case left = "<"
        case right = ">"

        init(rawValue: Character) {
            switch rawValue {
            case "<": self = .left
            case ">": self = .right
            case "v": self = .down
            case "^": self = .up
            default: fatalError()
            }
        }


        var dx: Int {
            switch self {
            case .up, .down: return 0
            case .left: return -1
            case .right: return 1
            }
        }


        var dy: Int {
            switch self {
            case .left, .right: return 0
            case .up: return -1
            case .down: return 1
            }
        }


        func newDirection(forTrackPart part: Character, turn: Turn) -> Direction {
            switch part {
            case "|":
                switch self {
                case .up, .down: return self
                default: fatalError()
                }
            case "-":
                switch self {
                case .left, .right: return self
                default: fatalError()
                }
            case "/":
                switch self {
                case .up, .down: return self.turnRight()
                case .left, .right: return self.turnLeft()
                }
            case "\\":
                switch self {
                case .up, .down: return self.turnLeft()
                case .left, .right: return self.turnRight()
                }
            case "+":
                return turn.newDirection(for: self)
            case " ":
                fatalError()
            default:
                fatalError()
            }
        }


        func turnLeft() -> Direction {
            switch self {
            case .down: return .right
            case .left: return .down
            case .right: return .up
            case .up: return .left
            }
        }


        func turnRight() -> Direction {
            switch self {
            case .down: return .left
            case .left: return .up
            case .right: return .down
            case .up: return .right
            }
        }
    }


    enum Turn {
        case left
        case right
        case straight

        var next: Turn {
            switch self {
            case .left: return .straight
            case .straight: return .right
            case .right: return .left
            }
        }


        func update(trackPart part: Character) -> Turn {
            if part == "+" {
                return next
            } else {
                return self
            }
        }


        func newDirection(for direction: Direction) -> Direction {
            switch self {
            case .straight: return direction
            case .left: return direction.turnLeft()
            case .right: return direction.turnRight()
            }
        }
    }

    private var x: Int
    private var y: Int
    private var direction: Direction
    private var turnState: Turn


    init(x: Int, y: Int, character: Character) {
        self.x = x
        self.y = y
        self.direction = Direction(rawValue: character)
        self.turnState = .left
    }


    var position: Coordinate {
        return Coordinate(x: x, y: y)
    }


    var nextPosition: Coordinate {
        return Coordinate(x: x + direction.dx, y: y + direction.dy)
    }


    var chr: Character {
        return direction.rawValue
    }


    func move(nextTrackPart part: Character) {
        x = nextPosition.x
        y = nextPosition.y
        direction = direction.newDirection(forTrackPart: part, turn: turnState)
        turnState = turnState.update(trackPart: part)
    }


    func isAt(coordinate: Coordinate) -> Bool {
        return position == coordinate
    }
}


extension Car {
    var trackPiece: Character {
        switch direction {
        case .up, .down: return "|"
        case .left, .right: return "-"
        }
    }
}


extension Car: CustomDebugStringConvertible {
    var debugDescription: String {
        return "Car(x: \(self.x), y: \(self.y), d: \(self.direction), t: \(self.turnState))"
    }
}
