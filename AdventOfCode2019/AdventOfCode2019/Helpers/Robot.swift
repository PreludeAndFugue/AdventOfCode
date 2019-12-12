//
//  Robot.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Robot {
    enum State {
        case paint
        case move
    }

    enum Colour: Int {
        case black = 0
        case white = 1
    }

    enum Turn: Int {
        case left = 0
        case right = 1
    }

    private let console: AutoConsole
    private let computer: Computer
    private var state: State
    private var direction: Direction
    private var coordinate: Coordinate
    private var panels: [Coordinate: Colour]

    init(memory: [Int], start: Colour) {
        console = AutoConsole(input: [start.rawValue])
        computer = Computer(memory: memory, console: console, runMode: .pauseAtOutput)
        state = .paint
        direction = .up
        coordinate = Coordinate(x: 0, y: 0)
        panels = [coordinate: start]
    }


    func start() {
        while !computer.isFinished {
            computer.run()
            switch state {
            case .move:
                move()
            case .paint:
                paint()
            }
        }
    }


    var panelsPainted: Int {
        return panels.count
    }


    var picture: String {
        let xCoords = Set(panels.keys.map({ $0.x }))
        let yCoords = Set(panels.keys.map({ $0.y }))
        var xMin = xCoords.min()!
        var xMax = xCoords.max()!
        var yMin = yCoords.min()!
        var yMax = yCoords.max()!
        let xOffset = xMin < 0 ? -xMin : 0
        xMax = xMax + xOffset
        xMin = xMin + xOffset
        let yOffset = yMin < 0 ? -yMin : 0
        yMax = yMax + yOffset
        yMin = yMin + yOffset
        var grid = Array(repeating: Array(repeating: " ", count: xMax + 1), count: yMax + 1)
        for (coord, colour) in panels {
            grid[coord.y + yOffset][coord.x + xOffset] = colour.debugDescription
        }
        grid.reverse()
        return grid.map({ $0.joined() }).joined(separator: "\n")
    }
}


// MARK: - Private

private extension Robot {
    func move() {
//        print("move")
        let output = console.getMostRecentOutput()
        let turn = Turn(rawValue: output)!
        direction = direction.turn(turn)
        coordinate = coordinate + direction.vector
        if let panelColour = panels[coordinate] {
            console.addInput(panelColour.rawValue)
        } else {
            panels[coordinate] = .black
            console.addInput(Colour.black.rawValue)
        }
        updateState()
    }


    func paint() {
//        print("paint")
        let output = console.getMostRecentOutput()
        let colour = Colour(rawValue: output)!
        panels[coordinate] = colour
        updateState()
    }


    private func updateState() {
        switch state {
        case .move:
            state = .paint
        case .paint:
            state = .move
        }
    }
}


extension Robot.Colour: CustomDebugStringConvertible {
    var debugDescription: String {
        switch self {
        case .black:
            return " "
        case .white:
            return "#"
        }
    }
}


private extension Direction {
    func turn(_ turn: Robot.Turn) -> Direction {
        switch turn {
        case .left:
            return turnLeft()
        case .right:
            return turnRight()
        }
    }
}
