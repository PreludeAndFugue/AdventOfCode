//
//  Day25.swift
//  AdventOfCode2016
//
//  Created by gary on 01/12/2022.
//

import Foundation

/// Answer from reverse engineering.
///
/// The first eight instructions set the value of register d.
/// The output of 0s and 1s is the binary digits of d.
///
/// cpy a d
/// cpy 15 c
/// cpy 170 b
/// inc d
/// dec b
/// jnz b -2
/// dec c
/// jnz c -5
///
/// When a is zero, d is set to 2550. The next number greater
/// than this that has alternating binary digits (101010) is
/// 2730.
///
/// If we set the initial value of a to 180, this will set d
/// to 2730 and the programme will output alternating 0s and
/// 1s.
///
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

    let input1 = """
cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
"""


    func run() {
        let compiler = Compiler()
        let instructions = compiler.compile(code: input)
        print(instructions)

        let computer = Computer()
        computer.load(instructions: instructions)

        computer.setRegisters(a: 180, b: 0, c: 0, d: 0)

        computer.run()
        print(computer.registers)
    }
}
