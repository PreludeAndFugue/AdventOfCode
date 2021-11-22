//
//  Problem17.swift
//  AdventOfCode2019
//
//  Created by gary on 20/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem17: Problem {
    private let file = "17/data17.txt"
    private lazy var input = {
        try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
    }()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 17, r1, r2)
    }
}


// MARK: - Private

private extension Problem17{
    private func part1() -> Int {
        let console = AutoConsole(input: [])
        let computer = Computer(memory: input, console: console)
        computer.run()
        var row = 0
        var column = 0
        var coords: Set<Coordinate> = []
        print(console.output.map({ Unicode.Scalar($0)! }).map({ String($0) }).joined())
        console.output.forEach({ intValue in
            let string = String(Unicode.Scalar(intValue)!)
            switch string {
            case "#":
                let coord = Coordinate(x: column, y: row)
                coords.insert(coord)
                column += 1
            case "\n":
                row += 1
                column = 0
            default:
                column += 1
            }
        })
        var intersections: [Coordinate] = []
        for coord in coords {
            let neighbours = coord.getGridNeighbours()
            if coords.intersection(neighbours).count == 4 {
                intersections.append(coord)
            }
        }
        let sum = intersections.map(alignmentParamater(_:)).sum()
        return sum
    }


    private func part2() -> Int {
        let instructions = answer.map({ Int($0.asciiValue!) })
        let console = AutoConsole(input: instructions)
        var memory = input
        memory[0] = 2
        let computer = Computer(memory: memory, console: console)
        computer.run()
        return console.output.last!
    }


    private func alignmentParamater(_ coordinate: Coordinate) -> Int {
        return coordinate.x * coordinate.y
    }
}


// A
private let a = "L,8,R,10,L,10"

// B
private let b = "R,10,L,8,L,8,L,10"

// C
private let c = "L,4,L,6,L,8,L,8"

// ROUTE
private let mainRoutine = "A,B,A,C,B,C,A,C,B,C"

private let answer = """
A,B,A,C,B,C,A,C,B,C
L,8,R,10,L,10
R,10,L,8,L,8,L,10
L,4,L,6,L,8,L,8
n

"""


//L,8,R,10,L,10,
//R,10,L,8,L,8,L,10,
//L,8,R,10,L,10,
//L,4,L,6,L,8,L,8,
//R,10,L,8,L,8,L,10,
//L,4,L,6,L,8,L,8,
//L,8,R,10,L,10,
//L,4,L,6,L,8,L,8,
//R,10,L,8,L,8,L,10,
//L,4,L,6,L,8,L,8
