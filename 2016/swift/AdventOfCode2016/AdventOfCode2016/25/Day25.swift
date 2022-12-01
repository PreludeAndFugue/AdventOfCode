//
//  Day25.swift
//  AdventOfCode2016
//
//  Created by gary on 01/12/2022.
//

import Foundation

class Day25 {
    let input = """
cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21
"""


    func run() {
        let compiler = Compiler()
        let instructions = compiler.compile(code: input)
        print(instructions)

        let computer = Computer()
        computer.load(instructions: instructions)

        computer.setRegisters(a: 10000, b: 0, c: 0, d: 0)

        computer.run()
    }
}
