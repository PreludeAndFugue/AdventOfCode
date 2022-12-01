//
//  Day23.swift
//  AdventOfCode2016
//
//  Created by gary on 01/12/2022.
//

import Foundation

class Day23 {
    let test1 = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""


    let input = """
cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 97 c
jnz 79 d
inc a
inc d
jnz d -2
inc c
jnz c -5
"""


    func run() {
        let compiler = Compiler()
        let instructions = compiler.compile(code: input)
        print(instructions)

        let computer = Computer()
        computer.load(instructions: instructions)

        computer.run()

        print(computer.registers)
    }
}
