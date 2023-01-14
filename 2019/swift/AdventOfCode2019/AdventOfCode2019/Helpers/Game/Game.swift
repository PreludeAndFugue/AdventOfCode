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

    private var sleep: UInt32? = nil
    var score = 0
    private var components: [Coordinate: Component] = [:]
    private let console: GameConsole
    private let computer: Computer
    private let screen: GameScreen?
    private var ballCoordinate: Coordinate?
    private var paddleCoordinate: Coordinate?


    init(data: [Int], screen: GameScreen?) {
        console = GameConsole()
        computer = Computer(memory: data, console: console)
        self.screen = screen
        console.add(delegate: self)
    }


    var blockCount: Int {
        components.filter({ $0.value == .block }).count
    }


    func run() {
        computer.run()
    }
}


// MARK: - GameConsoleDelegate

extension Game: GameConsoleDelegate {
    func receive(triplet: GameConsole.Triplet, from console: GameConsole) {
        if triplet.x == -1 {
            score = triplet.c
        } else {
            let (coordinate, component) = makeComponent(from: triplet)
            components[coordinate] = component
        }
        screen?.draw(components: components, score: score, sleep: sleep)
    }


    func inputRequest(from console: GameConsole) {
        sleep = 6_000
        guard let ball = ballCoordinate, let paddle = paddleCoordinate else {
            console.addInput(0)
            return
        }
        if ball.x < paddle.x {
            console.addInput(-1)
        } else if ball.x == paddle.x {
            console.addInput(0)
        } else {
            console.addInput(1)
        }
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
    private func makeComponent(from triplet: GameConsole.Triplet) -> (Coordinate, Component) {
        let coordinate = Coordinate(x: triplet.x, y: triplet.y)
        let component = Component(rawValue: triplet.c)!
        switch component {
        case .ball: ballCoordinate = coordinate
        case .paddle: paddleCoordinate = coordinate
        default: break
        }
        return (coordinate, component)
    }
}
