//
//  Day11.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation

func day11() {
    let program = getIncode(file: "11")

    let p1 = part1(program: program)
    print(p1)

    part2(program: program)
}


private func part1(program: IntCode) -> Int {
    let c = Computer()
    c.load(program: program)
    c.input.append(0)
    let map = run(computer: c)
    return map.count
}


private func part2(program: IntCode) {
    let c = Computer()
    c.load(program: program)
    c.input.append(1)
    let map = run(computer: c)
    print(map: map)
}


private func run(computer: Computer) -> [Point: Int] {
    var map: [Point: Int] = [:]
    var position = Point.origin
    var direction = Direction.up

    while true {
        computer.run()
        computer.run()
        if computer.state == .done {
            break
        }
        let paint = computer.output.removeFirst()
        let turn = computer.output.removeFirst()
        map[position] = paint

        direction = direction.turn(turn)
        position = position + direction.diff

        let a = map[position, default: 0]
        computer.input.append(a)
    }
    return map
}


private func print(map: [Point: Int]) {
    var xs: [Int] = []
    var ys: [Int] = []
    for point in map.keys {
        xs.append(point.x)
        ys.append(point.y)
    }
    let minX = xs.min()!
    let maxX = xs.max()!
    let minY = ys.min()!
    let maxY = ys.max()!
    let yRange = stride(from: maxY, through: minY, by: -1)
    for y in yRange {
        var row: [String] = []
        for x in minX...maxX {
            let p = Point(x: x, y: y)
            let paint = map[p, default: 0]
            if paint == 1 {
                row.append("⬜️")
            } else {
                row.append("⬛️")
            }
        }
        print(row.joined())
    }
}


private enum Direction {
    case up
    case down
    case left
    case right


    var diff: Point {
        switch self {
        case .up: return Point(x: 0, y: 1)
        case .down: return Point(x: 0, y: -1)
        case .left: return Point(x: -1, y: 0)
        case .right: return Point(x: 1, y: 0)
        }
    }


    func turn(_ n: Int) -> Direction {
        switch (self, n) {
        case (.up, 0): return .left
        case (.up, 1): return .right
        case (.down, 0): return .right
        case (.down, 1): return .left
        case (.left, 0): return .down
        case (.left, 1): return .up
        case (.right, 0): return .up
        case (.right, 1): return .down
        default:
            fatalError()
        }
    }
}
