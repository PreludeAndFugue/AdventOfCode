//
//  MazeScreen.swift
//  AdventOfCode2019
//
//  Created by gary on 18/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Darwin

final class MazeScreen {
    let map: Set<Coordinate>
    let oxygenSpread: [[Coordinate]]
    var time = 0
    var screen: [[String]]
    let xMin: Int
    let yMin: Int

    init(map: Set<Coordinate>, oxygenSpread: [[Coordinate]]) {
        self.map = map
        self.oxygenSpread = oxygenSpread
        let xCoords = map.map({ $0.x })
        let yCoords = map.map({ $0.y })
        let (xMin, xMax) = (xCoords.min()!, xCoords.max()!)
        let (yMin, yMax) = (yCoords.min()!, yCoords.max()!)
        screen = Array(
            repeating: Array(repeating: "#", count: xMax - xMin + 3),
            count: yMax - yMin + 3
        )
        for coord in map {
            screen[coord.y - yMin + 1][coord.x - xMin + 1] = " "
        }
        self.xMin = xMin
        self.yMin = yMin
    }


    func draw() {
        for oxygen in oxygenSpread {
            draw(oxygen: oxygen)
            usleep(100_000)
        }
    }


    private func draw(oxygen: [Coordinate]) {
        for coord in oxygen {
            screen[coord.y - yMin + 1][coord.x - xMin + 1] = "."
        }
        print("\u{001B}[2J")
        print(screen.map({ $0.joined() }).joined(separator: "\n"))
    }
}
