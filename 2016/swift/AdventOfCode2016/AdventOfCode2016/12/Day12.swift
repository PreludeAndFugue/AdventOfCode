//
//  Day12.swift
//  AdventOfCode2016
//
//  Created by gary on 30/11/2022.
//

import Foundation

struct Data12 {
    static let test1 = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

    static let input = """
cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 12 d
inc a
dec d
jnz d -2
dec c
jnz c -5
"""
}

class Day12 {
    func run() {
        let compiler = Compiler()
        let instructions = compiler.compile(code: Data12.input)
        print(instructions)

        let computer = Computer()
        computer.load(instructions: instructions)
        computer.setRegisters(a: 0, b: 0, c: 1, d: 0)
        computer.run()
        print(computer.registers)
    }
}
