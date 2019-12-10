//
//  Problem03.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//


final class Problem03: Problem {
    private let file = "3/data03.txt"
    private lazy var input = self.makeInput()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(r1, r2)
    }
}


// MARK: - Private

private extension Problem03 {
    private func makeInput() -> [[Instruction]] {
        let string = try! String(contentsOfFile: path + file)
        return Instruction.make(fromString: string)
    }


    private func part1() -> Int {
        let instructions1 = input[0]
        let instructions2 = input[1]
        let coords1 = getCoordinates(from: instructions1)
        let coords2 = getCoordinates(from: instructions2)
        let smallestDistance = Set(coords1).intersection(coords2)
            .map({ $0.manhattanDistanceFromOrigin })
            .sorted()
            .first!
        return smallestDistance
    }


    private func part2() -> Int {
        let instructions1 = input[0]
        let instructions2 = input[1]
        let coords1 = getCoordinates(from: instructions1)
        let coords2 = getCoordinates(from: instructions2)
        let intersection = Set(coords1).intersection(coords2)
        let coordsWithSteps1 = coords1.enumerated().map({ ($0.offset + 1, $0.element) })
        let coordsWithSteps2 = coords2.enumerated().map({ ($0.offset + 1, $0.element) })
        var minSteps = Int.max
        for coord in intersection {
            for (s1, c1) in coordsWithSteps1 {
                guard c1 == coord else { continue }
                for (s2, c2) in coordsWithSteps2 {
                    guard c2 == coord else { continue }
                    let steps = s1 + s2
                    if steps == minSteps {
                        print("steps == minSteps")
                    }
                    if steps < minSteps {
                        minSteps = steps
                    }
                }
            }
        }
        return minSteps
    }


    private func getCoordinates(from instructions: [Instruction]) -> [Coordinate] {
        var coords: [Coordinate] = []
        var current = Coordinate.origin
        for instruction in instructions {
            for _ in 0..<instruction.length {
                current = current + instruction.direction.vector
                coords.append(current)
            }
        }
        return coords
    }
}


// MARK: - Test input

private var input1: [[Instruction]] = {
    let string = "R8,U5,L5,D3\nU7,R6,D4,L4"
    return Instruction.make(fromString: string)
}()


private var input2: [[Instruction]] = {
    let string = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
    return Instruction.make(fromString: string)
}()


private var input3: [[Instruction]] = {
    let string = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    return Instruction.make(fromString: string)
}()


// MARK: - Instruction

private struct Instruction: CustomDebugStringConvertible {
    let direction: Direction
    let length: Int

    init(rawInput: String) {
        self.direction = Direction(directionString: String(rawInput.first!))
        self.length = Int(String(rawInput.dropFirst()))!
    }

    var debugDescription: String {
        return "I(\(direction), \(length))"
    }


    static func make(fromString string: String) -> [[Instruction]] {
        return string
            .components(separatedBy: "\n")
            .filter({ !$0.isEmpty })
            .map({ $0.components(separatedBy: ",")
            .map(Instruction.init) })
    }
}
