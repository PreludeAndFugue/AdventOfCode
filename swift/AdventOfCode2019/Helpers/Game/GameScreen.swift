//
//  GameScreen.swift
//  AdventOfCode2019
//
//  Created by gary on 14/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Darwin

struct GameScreen {
    func draw(components: [Coordinate: Game.Component], score: Int, sleep: UInt32?) {
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

        print("\u{001B}[2J")
        print("Score: \(score)")
        print(screen.map({ $0.joined() }).joined(separator: "\n"))
        if let sleep = sleep {
            usleep(sleep)
        }
    }
}
