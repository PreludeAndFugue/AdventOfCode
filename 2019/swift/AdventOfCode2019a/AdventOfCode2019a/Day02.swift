//
//  Day02.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

func day02() {
    let program = getIncode(file: "02")

    let p1 = part1(program: program)
    print(p1)

    let p2 = part2(progam: program)
    print(p2)
}


func part1(program: IntCode) -> Int {
    var p = program
    p[1] = 12
    p[2] = 2
    let c = Computer()
    c.load(program: p)
    c.run()
    return c.memory[0]
}


func part2(progam: IntCode) -> Int {
    let c = Computer()
    for noun in 0..<100 {
        for verb in 0..<100 {
            var p = progam
            p[1] = noun
            p[2] = verb
            c.load(program: p)
            c.run()
            let n = c.memory[0]
            if n == 19690720 {
                return 100 * noun + verb
            }
        }
    }
    fatalError()
}
