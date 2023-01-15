//
//  Day07.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation
import Algorithms

func day07() {
//    let program = test5.trimmingCharacters(in: .whitespacesAndNewlines)
//        .split(separator: ",")
//        .map({ Int($0)! })
    let program = getIncode(file: "07")

    let p1 = part1(program: program)
    print(p1)

    let p2 = part2(program: program)
    print(p2)
}


private func part1(program: IntCode) -> Int {
    let phaseValues = 0...4
    var inputSignal = 0
    var maxSignal = 0
    let c = Computer()
    for phases in phaseValues.permutations() {
        inputSignal = 0
        for phase in phases {
            c.load(program: program)
            let input = [phase, inputSignal]
            c.input.append(contentsOf: input)
            c.run()
            inputSignal = c.output.last!
        }
        maxSignal = max(maxSignal, inputSignal)
    }
    return maxSignal
}


private func part2(program: IntCode) -> Int {
    var maxResult = 0
    for phases in (5...9).permutations() {
        let result = run2(program: program, phases: phases)
        maxResult = max(maxResult, result)
    }
    return maxResult
}


private func run2(program: IntCode, phases: [Int]) -> Int {
    var inputSignal = 0
    let computers = [Computer(), Computer(), Computer(), Computer(), Computer()]
    for (c, p) in zip(computers, phases) {
        c.load(program: program)
        c.input.append(p)
    }
    while !allDone(computers: computers) {
        for c in computers {
            c.input.append(inputSignal)
            c.run()
            inputSignal = c.output.last!
        }
    }
    return inputSignal
}


private func allDone(computers: [Computer]) -> Bool {
    for c in computers {
        if c.state != .done {
            return false
        }
    }
    return true
}


private let test1 = """
3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
"""
private let phases1 = [4, 3, 2, 1, 0]

private let test2 = """
3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0
"""
private let phases2 = [0, 1, 2, 3, 4]

private let test3 = """
3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
"""
private let phases3 = [1, 0, 4, 3, 2]

private let test4 = """
3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
"""
private let phases4 = [9, 8, 7, 6, 5]

private let test5 = """
3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
"""

