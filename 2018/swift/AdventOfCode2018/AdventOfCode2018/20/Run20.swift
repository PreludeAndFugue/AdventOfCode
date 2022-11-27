//
//  Run20.swift
//  AdventOfCode2018
//
//  Created by gary on 27/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation

extension Coordinate {
    func north() -> Coordinate { Coordinate(x: x, y: y - 1)}
    func south() -> Coordinate { Coordinate(x: x, y: y + 1)}
    func west() -> Coordinate { Coordinate(x: x - 1, y: y)}
    func east() -> Coordinate { Coordinate(x: x + 1, y: y)}
}


private struct Position: Hashable {
    enum PositionType {
        case doorVertical
        case doorHorizontal
        case path

        var ch: String {
            switch self {
            case .path: return "."
            case .doorVertical: return "-"
            case .doorHorizontal: return "|"
            }
        }

        var isDoor: Bool {
            switch self {
            case .doorVertical, .doorHorizontal: return true
            case .path: return false
            }
        }

        func nextVertical() -> PositionType {
            switch self {
            case .doorVertical: return .path
            case .doorHorizontal: fatalError()
            case .path: return .doorVertical
            }
        }

        func nextHorizontal() -> PositionType {
            switch self {
            case .doorVertical: fatalError()
            case .doorHorizontal: return .path
            case .path: return .doorHorizontal
            }
        }
    }

    let coord: Coordinate
    let type: PositionType
    let distance: Int

    func north() -> Position {
        let newCoord = Coordinate(x: coord.x, y: coord.y - 1)
        let newDistance = type.isDoor ? distance + 1 : distance
        return Position(coord: newCoord, type: type.nextVertical(), distance: newDistance)
    }


    func south() -> Position {
        let newCoord = Coordinate(x: coord.x, y: coord.y + 1)
        let newDistance = type.isDoor ? distance + 1 : distance
        return Position(coord: newCoord, type: type.nextVertical(), distance: newDistance)
    }


    func east() -> Position {
        let newCoord = Coordinate(x: coord.x + 1, y: coord.y)
        let newDistance = type.isDoor ? distance + 1 : distance
        return Position(coord: newCoord, type: type.nextHorizontal(), distance: newDistance)
    }


    func west() -> Position {
        let newCoord = Coordinate(x: coord.x - 1, y: coord.y)
        let newDistance = type.isDoor ? distance + 1 : distance
        return Position(coord: newCoord, type: type.nextHorizontal(), distance: newDistance)
    }


    func hash(into hasher: inout Hasher) {
        hasher.combine(coord)
    }
}


private func maxPosition(_ positions: [Coordinate: Position]) -> Int {
    positions.values.map({ $0.distance }).max() ?? 0
}


private func print(positions: [Coordinate: Position]) -> String {
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
    var position = Position(coord: Coordinate(x: 0, y: 0), type: .path, distance: 0)
    var positions: [Coordinate: Position] = [position.coord: position]

    for ch in data20 {
        switch ch {
        case "N":
            for _ in 0..<2 {
                position = position.north()
                if !positions.contains(where: { $0.key == position.coord}) {
                    positions[position.coord] = position
                }
            }
        case "S":
            for _ in 0..<2 {
                position = position.south()
                if !positions.contains(where: { $0.key == position.coord}) {
                    positions[position.coord] = position
                }
            }
        case "E":
            for _ in 0..<2 {
                position = position.east()
                if !positions.contains(where: { $0.key == position.coord}) {
                    positions[position.coord] = position
                }
            }
        case "W":
            for _ in 0..<2 {
                position = position.west()
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

//    print(positions)

    let s = print(positions: positions)
//    print(s)
    let m = maxPosition(positions)
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
