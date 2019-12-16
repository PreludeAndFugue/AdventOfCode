//
//  DroidController.swift
//  AdventOfCode2019
//
//  Created by gary on 15/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class DroidController {
    private let droid: RepairDroid
    var map: Set<Coordinate>
    private var position: Coordinate
    var oxygenSystemPosition: Coordinate?
    private var direction: Direction

    init(memory: [Int]) {
        let console = RepairDroid.DroidConsole()
        droid = RepairDroid(memory: memory, console: console)
        position = Coordinate(x: 0, y: 0)
        map = [position]
        direction = .up
        console.add(delegate: self)
    }


    func run() {
        droid.run()
        print(drawMap())
    }
}


// MARK: - DroidConsoleDelegate

extension DroidController: DroidConsoleDelegate {
    func receive(output: RepairDroid.Output, from console: RepairDroid.DroidConsole) {
//        print("robot output:", output)
        switch output {
        case .blocked:
            direction = direction.turnLeft()
        case .moved:
            position = position + direction.vector
            map.insert(position)
            direction = direction.turnRight()
        case .foundOxygenSystem:
            position = position + direction.vector
            map.insert(position)
            oxygenSystemPosition = position
            droid.stop()
        }
    }

    func inputRequest(from console: RepairDroid.DroidConsole) {
//        print("robot command:", direction.robotDirection)
        console.add(command: direction.robotDirection)
    }
}


// MARK: - Direction

private extension Direction {
    var robotDirection: RepairDroid.Command {
        switch self {
        case .up:
            return .north
        case .down:
            return .south
        case .left:
            return .west
        case .right:
            return .east
        }
    }
}


// MARK: - Private

private extension DroidController {
    func drawMap() -> String {
        let xCoords = map.map({ $0.x })
        let (xMin, xMax) = (xCoords.min()!, xCoords.max()!)
        let yCoords = map.map({ $0.y })
        let (yMin, yMax) = (yCoords.min()!, yCoords.max()!)
        let xCount = xMax - xMin + 3
        let yCount = yMax - yMin + 3
        var grid = Array(repeating: Array(repeating: " ", count: xCount), count: yCount)
        for coord in map {
            grid[coord.y - yMin + 1][coord.x - xMin + 1] = getMapSymbol(for: coord)
        }
        return grid.map({ $0.joined() }).joined(separator: "\n")
    }


    func getMapSymbol(for coordinate: Coordinate) -> String {
        if coordinate.isOrigin {
            return "S"
        } else if coordinate == oxygenSystemPosition {
            return "X"
        } else {
            return "*"
        }
    }
}
