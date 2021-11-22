//
//  Run19.swift
//  AdventOfCode2018
//
//  Created by gary on 30/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

func run19() {
//    test19a()
//    main19a()
    test19b()
}


func main19a() {
    run(data: data19)
}


func test19a() {
    run(data: testData19)
}


func test19b() {
    let num = 10_551_340;
    var sum = 0;
    for i in 1...num {
        if num % i == 0 {
            sum += i;
        }
    }
    print(sum)
}


private func run(data: String) {
    let parser = Parser19()
    let registers = Registers(number: 6)
    let (pointerRegister, instructions) = parser.parse(data: data)
    var pointer = 0


    // Part 2
    registers.set(0, value: 1)

    while true {
        if pointer < instructions.startIndex || pointer >= instructions.endIndex { break }

        registers.set(pointerRegister, value: pointer)
        let instruction = instructions[pointer]

        let oldPointer = pointer
        let oldRegisters = registers.debugDescription

        instruction.evaluate(registers: registers)
        pointer = registers.get(pointerRegister) + 1

//        print(oldPointer, oldRegisters, instruction, registers)
        print(oldPointer, registers)
    }
    print("answer", registers.get(0))
}
