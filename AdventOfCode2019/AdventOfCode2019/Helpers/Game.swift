//
//  Game.swift
//  AdventOfCode2019
//
//  Created by gary on 14/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Game {
    enum Component: Int {
        case empty = 0
        case wall = 1
        case block = 2
        case paddle = 3
        case ball = 4
    }

    private let components: [Coordinate: Component]


    init(data: [Int]) {
        let dictData = triplets(data).map({ (Coordinate(x: $0.x, y: $0.y), Component(rawValue: $0.c)!) })
        components = Dictionary(uniqueKeysWithValues: dictData)
    }


    var blockCount: Int {
        components.filter({ $0.value == .block }).count
    }


    func draw() -> String {
        let xCoords = components.keys.map({ $0.x })
        let yCoords = components.keys.map({ $0.y })
        let (xMin, xMax) = (xCoords.min()!, xCoords.max()!)
        let (yMin, yMax) = (yCoords.min()!, yCoords.max()!)
        assert(xMin >= 0)
        assert(yMin >= 0)
        var screen = Array(repeating: Array(repeating: "", count: xMax + 1), count: yMax + 1)
        for (coord, component) in components {
            screen[coord.y][coord.x] = component.graphic
        }
        return screen.map({ $0.joined() }).joined(separator: "\n")
    }
}


// MARK: - Game.Component

extension Game.Component {
    var graphic: String {
        switch self {
        case .empty:
            return " "
        case .wall:
            return "#"
        case .block:
            return "x"
        case .paddle:
            return "-"
        case .ball:
            return "o"
        }
    }
}


// MARK: - Private

private extension Game {

}

private typealias Triplet = (x: Int, y: Int, c: Int)

private func triplets(_ numbers: [Int]) -> [Triplet] {
    var result: [Triplet] = []
    var triplet: [Int] = []
    for (i, n) in numbers.enumerated() {
        triplet.append(n)
        if i % 3 == 2 {
            result.append((x: triplet[0], y: triplet[1], c: triplet[2]))
            triplet = []
        }
    }
    return result
}
