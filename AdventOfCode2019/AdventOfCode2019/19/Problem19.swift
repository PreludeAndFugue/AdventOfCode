//
//  Problem19.swift
//  AdventOfCode2019
//
//  Created by gary on 23/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem19: Problem {
    private let file = "19/data19.txt"
    private lazy var input = { try! String(contentsOfFile: path + file).makeIntegers(separator: ",") }()

    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 19, r1, r2)
    }
}


// MARK: - Private

private extension Problem19 {
    private typealias BeamValue = (Coordinate, Int)

    private func part1() -> Int {
        print(input)
        let coordinates = makeCoordinates()
        var values: [BeamValue] = []
        for coordinate in coordinates {
            let console = AutoConsole(input: [coordinate.x, coordinate.y])
            let computer = Computer(memory: input, console: console)
            computer.run()
            values.append((coordinate, console.output.first!))
        }

        display(beamValues: values)
        return values.map({ $0.1 }).sum()
    }


    private func makeCoordinates() -> [Coordinate] {
        var coordinates: [Coordinate] = []
        for x in 0..<50 {
            for y in 0..<50 {
                coordinates.append(Coordinate(x: x, y: y))
            }
        }
        return coordinates
    }


    private func makeConsoleInput(from coordinates: [Coordinate]) -> [Int] {
        coordinates.map({ [$0.x, $0.y] }).flatMap({ $0 })
    }


    private func display(beamValues: [BeamValue]) {
        let coordinates = beamValues.map({ $0.0 })
        let xCoords = coordinates.map({ $0.x })
        let yCoords = coordinates.map({ $0.y })
        let (xMin, xMax) = (xCoords.min()!, xCoords.max()!)
        let (yMin, yMax) = (yCoords.min()!, yCoords.max()!)
        var screen = Array(repeating: Array(repeating: "", count: xMax + 1), count: yMax + 1)
        for (coord, value) in beamValues {
            screen[coord.y][coord.x] = value == 0 ? "." : "#"
        }
        let display = screen.map({ $0.joined() }).joined(separator: "\n")
        print(display)
    }
}
