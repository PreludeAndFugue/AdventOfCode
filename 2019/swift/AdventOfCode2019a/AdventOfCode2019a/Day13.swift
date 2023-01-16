//
//  Day13.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation

func day13() {
    let program = getIncode(file: "13")

    let p1 = part1(program: program)
    print(p1)

    let p2 = part2(program: program)
    print(p2)
}


private func part1(program: IntCode) -> Int {
    let io = GameTestIO()
    let c = Computer(io: io)
    c.load(program: program)
    c.run()
    return io.blockCounter
}


private func part2(program: IntCode) -> Int {
    let io = GameIO()
    let c = Computer(io: io)
    c.load(program: program)
    c.memory[0] = 2
    c.run()
    return io.score
}
