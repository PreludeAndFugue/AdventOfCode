//
//  Problem19.swift
//  AdventOfCode2019
//
//  Created by gary on 23/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

/// Part 2
/// ------
///
/// y = 700, beam width = 119
///
///
/// First attempt: 8020999, too low
///
///
final class Problem19: Problem {
    private typealias BeamValue = (Coordinate, Int)
    private typealias RowCache = [Int: (xMin: Int, xMax: Int)]

    private let file = "19/data19.txt"
    private lazy var input = { try! String(contentsOfFile: path + file).makeIntegers(separator: ",") }()

    // For part 2
    private var cache: RowCache = [:]
    private let width = 100

    func run() {
        let r1 = 0
//        let r1 = part1()
//        let r2 = 0
        let r2 = part2()
        printResults(number: 19, r1, r2)
    }
}


// MARK: - Private

private extension Problem19 {
    private func part1() -> Int {
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


    private func part2() -> Int {
        var xAnswer = 0
        var yAnswer = 0
        for y in 1000...1500 {
            let (xMin1, xMax1) = getRowValues(y: y)
            let count1 = xMax1 - xMin1 + 1
            if count1 < width {
                continue
            }
            let (xMin2, xMax2) = getRowValues(y: y + width - 1)

//            print(y, xMin1, xMax1)
//            print(xMin2, xMax2)

            let count2 = xMax1 - xMin2 + 1
            if count2 == width {
                print("y", y, "xMin2", xMin2)
                print(10_000 * xMin2 + y)

                print(y - 1, cache[y - 1])
                print(y + width - 2, cache[y + width - 2])
                print("---")
                print(y, cache[y])
                print(y + width - 1, cache[y + width - 1])
                print("---")

                xAnswer = xMin2
                yAnswer = y
                break
            }
        }
        return 10_000 * xAnswer + yAnswer
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


    private func getRowValues(y: Int) -> (xMin: Int, xMax: Int) {
        if let row = cache[y] {
            return row
        }
        var x = 0
        var seenXMin = false
        var xMin = 0
        var xMax = 0
        while true {
            let console = AutoConsole(input: [x, y])
            let computer = Computer(memory: input, console: console)
            computer.run()
            let value = console.output.first!
            if value == 1 && !seenXMin {
                xMin = x
                seenXMin = true
            } else if value == 0 && seenXMin {
                xMax = x - 1
                break
            }
            x += 1
        }
        cache[y] = (xMin, xMax)
        return (xMin, xMax)
    }


    private func display(beamValues: [BeamValue]) {
        let coordinates = beamValues.map({ $0.0 })
        let xCoords = coordinates.map({ $0.x })
        let yCoords = coordinates.map({ $0.y })
        let xMax = xCoords.max()!
        let yMax = yCoords.max()!
        var screen = Array(repeating: Array(repeating: "", count: xMax + 1), count: yMax + 1)
        for (coord, value) in beamValues {
            screen[coord.y][coord.x] = value == 0 ? "." : "#"
        }
        let display = screen.map({ $0.joined() }).joined(separator: "\n")
        print(display)
    }
}
