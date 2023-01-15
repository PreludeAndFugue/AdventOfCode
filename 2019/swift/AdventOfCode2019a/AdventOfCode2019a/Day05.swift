//
//  Day05.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

private let test1 = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".trimmingCharacters(in: .whitespacesAndNewlines)
    .split(separator: ",")
    .map({ Int($0)! })


func day05() {
    let program = getIncode(file: "05")

    let p1 = part1(program: program)
    print(p1)

    let p2 = part2(program: program)
    print(p2)
}


private func part1(program: IntCode) -> Int {
    let c = Computer()
    c.load(program: program)
    c.input.append(1)
    c.run()
    var output = c.output
    let n = output.popLast()!
    for i in output {
        assert(i == 0)
    }
    return n
}


private func part2(program: IntCode) -> Int {
    let c = Computer()
    c.load(program: program)
    c.input.append(5)
    c.run()
    return c.output.first!
}
