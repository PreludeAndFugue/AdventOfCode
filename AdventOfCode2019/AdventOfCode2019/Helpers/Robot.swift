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

    init(memory: [Int]) {
        console = AutoConsole(input: [0])
        computer = Computer(memory: memory, console: console, runMode: .pauseAtOutput)
        state = .paint
        direction = .up
        coordinate = Coordinate(x: 0, y: 0)
        panels = [coordinate: .black]
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
