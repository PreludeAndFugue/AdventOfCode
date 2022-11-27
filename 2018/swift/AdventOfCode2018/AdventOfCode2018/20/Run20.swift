//
//  Run20.swift
//  AdventOfCode2018
//
//  Created by gary on 27/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation

private enum Direction: Character {
    case N = "N"
    case S = "S"
    case E = "E"
    case W = "W"

    var dx: Int {
        switch self {
        case .N, .S: return 0
        case .E: return 1
        case .W: return -1
        }
    }

    var dy: Int {
        switch self {
        case .N: return -1
        case .S: return 1
        case .E, .W: return 0
        }
    }

    var isVertical: Bool {
        switch self {
        case .N, .S: return true
        case .E, .W: return false
        }
    }
}

private struct Position: Hashable {
    enum PositionType {
        case doorVertical
        case doorHorizontal
        case room

        var ch: String {
            switch self {
            case .room: return "."
            case .doorVertical: return "-"
            case .doorHorizontal: return "|"
            }
        }

        var isDoor: Bool {
            switch self {
            case .doorVertical, .doorHorizontal: return true
            case .room: return false
            }
        }

        func nextVertical() -> PositionType {
            switch self {
            case .doorVertical: return .room
            case .doorHorizontal: fatalError()
            case .room: return .doorVertical
            }
        }

        func nextHorizontal() -> PositionType {
            switch self {
            case .doorVertical: fatalError()
            case .doorHorizontal: return .room
            case .room: return .doorHorizontal
            }
        }
    }

    let coord: Coordinate
    let type: PositionType
    let distance: Int

    func move(_ direction: Direction) -> Position {
        let newCoord = Coordinate(x: coord.x + direction.dx, y: coord.y + direction.dy)
        let newDistance = type.isDoor ? distance + 1 : distance
        let newType = direction.isVertical ? type.nextVertical() : type.nextHorizontal()
        return Position(coord: newCoord, type: newType, distance: newDistance)
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(coord)
    }
}


private func asString(positions: [Coordinate: Position]) -> String {
    let start = Coordinate(x: 0, y: 0)
    let xs = positions.keys.map({ $0.x })
    let ys = positions.keys.map({ $0.y })
    let minX = xs.min()! - 1
    let maxX = xs.max()! + 1
    let minY = ys.min()! - 1
    let maxY = ys.max()! + 1
    var rows: [String] = []
    for y in minY...maxY {
        var row: [String] = []
        for x in minX...maxX {
            let c = Coordinate(x: x, y: y)
            if let p = positions[c] {
                if p.coord == start {
                    row.append("X")
                } else {
                    row.append(p.type.ch)
                }
            } else {
                row.append("#")
            }
        }
        rows.append(row.joined())
    }
    return rows.joined(separator: "\n")
}


func run20() {
    var stack: [Position] = []
    var position = Position(coord: Coordinate(x: 0, y: 0), type: .room, distance: 0)
    var positions: [Coordinate: Position] = [position.coord: position]

    for ch in data20 {
        switch ch {
        case "N", "S", "E", "W":
            for _ in 0..<2 {
                let direction = Direction(rawValue: ch)!
                position = position.move(direction)
                if !positions.contains(where: { $0.key == position.coord}) {
                    positions[position.coord] = position
                }
            }
        case "|":
            position = stack.last!
        case "(":
            stack.append(position)
        case ")":
            _ = stack.popLast()
        case "^", "$":
            continue
        default:
            assertionFailure()
        }
    }

    assert(stack.isEmpty)

//    let s = asString(positions: positions)
//    print(s)
    let m = positions.values.map({ $0.distance }).max() ?? 0
    print(m)

    var count = 0
    for (_, v) in positions {
        if !v.type.isDoor && v.distance >= 1000 {
            count += 1
        }
    }
    print(count)
}


let test1 = "^WNE$"

let test2 = "^ENWWW(NEEE|SSE(EE|N))$"

let test3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"

let test4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"

let test5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
