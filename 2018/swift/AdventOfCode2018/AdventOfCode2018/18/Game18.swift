//
//  Game18.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Game18 {
    private let openAcre: Character = "."
    private let treeAcre: Character = "|"
    private let lumberYardAcre: Character = "#"

    private let width: Int
    private let height: Int
    private var map: [Coordinate: Character]


    init(data: String) {
        var map: [Coordinate: Character] = [:]
        for (y, row) in data.split(separator: "\n").enumerated() {
            for (x, item) in row.enumerated() {
                let coordinate = Coordinate(x: x, y: y)
                map[coordinate] = item
            }
        }
        self.width = data.split(separator: "\n").first?.count ?? 0
        self.height = data.split(separator: "\n").count
        self.map = map
    }


    func run(steps: Int) {
        for _ in 0..<steps {
            step()
        }
    }


    func step() {
        var newMap: [Coordinate: Character] = [:]
        for (coord, value) in map {
            let n = neighbours(of: coord)
            newMap[coord] = update(value: value, neighbours: n)
        }
        self.map = newMap
    }


    var resourceValue: Int {
        let lumberYardCount = map.values.filter({ $0 == lumberYardAcre }).count
        let treeCount = map.values.filter({ $0 == treeAcre }).count
        return lumberYardCount * treeCount
    }
}


private extension Game18 {
    func neighbours(of coordinate: Coordinate) -> [Character] {
        var values: [Character] = []
        for n in coordinate.neighbours() {
            if let value = map[n] {
                values.append(value)
            }
        }
        return values
    }


    func update(value: Character, neighbours: [Character]) -> Character {
        switch value {
        case openAcre:
            return updateOpen(neighbours)
        case treeAcre:
            return updateTrees(neighbours)
        case lumberYardAcre:
            return updateLumberyard(neighbours)
        default:
            fatalError()
        }
    }


    func updateOpen(_ neighbours: [Character]) -> Character {
        if neighbours.filter({ $0 == treeAcre }).count >= 3 {
            return treeAcre
        } else {
            return openAcre
        }
    }


    func updateTrees(_ neighbours: [Character]) -> Character {
        if neighbours.filter({ $0 == lumberYardAcre }).count >= 3 {
            return lumberYardAcre
        } else {
            return treeAcre
        }
    }


    func updateLumberyard(_ neighbours: [Character]) -> Character {
        let lumberYardCount = neighbours.filter({ $0 == lumberYardAcre }).count
        let treeCount = neighbours.filter({ $0 == treeAcre }).count
        if lumberYardCount >= 1 && treeCount >= 1 {
            return lumberYardAcre
        } else {
            return openAcre
        }
    }
}


extension Game18: CustomDebugStringConvertible {
    var debugDescription: String {
        var values: [[String]] = []
        for y in 0..<height {
            var row: [String] = []
            for x in 0..<width {
                let coordinate = Coordinate(x: x, y: y)
                row.append(String(map[coordinate]!))
            }
            values.append(row)
        }
        return values.map({ $0.joined() }).joined(separator: "\n")
    }
}
