//
//  Day07.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation
import Algorithms

func day07() {
    let program = getIncode(file: "07")

    let p1 = part1(program: program)
    print(p1)
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
