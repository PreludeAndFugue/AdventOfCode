//
//  Computer.swift
//  AdventOfCode2016
//
//  Created by gary on 30/11/2022.
//

import Foundation

enum Instruction: CustomDebugStringConvertible {
    case cpy(Int, String)
    case cpyValue(String, String)
    case inc(String)
    case dec(String)
    case jnz(String, Int)


    var debugDescription: String {
        switch self {
        case .cpy(let a, let b): return "cpy \(a) \(b)"
        case .cpyValue(let a, let b): return "cpy \(a) \(b)"
        case .inc(let a): return "inc \(a)"
        case .dec(let a): return "dec \(a)"
        case .jnz(let a, let b): return "jnz \(a) \(b)"
        }
    }
}


class Compiler {
    func compile(code: String) -> [Instruction] {
        var instructions: [Instruction] = []
        for line in code.trimmingCharacters(in: .whitespaces).split(separator: "\n") {
            let parts = line.split(separator: " ")
            if line.starts(with: "cpy") {
                let register = String(parts[1])
                let register2 = String(parts[2])
                if register.first?.isNumber == true {
                    let instruction = Instruction.cpy(Int(register)!, register2)
                    instructions.append(instruction)
                } else {
                    let instruction = Instruction.cpyValue(register, register2)
                    instructions.append(instruction)
                }
            } else if line.starts(with: "inc") {
                let register = String(parts[1])
                let instruction = Instruction.inc(register)
                instructions.append(instruction)
            } else if line.starts(with: "dec") {
                let register = String(parts[1])
                let instruction = Instruction.dec(register)
                instructions.append(instruction)
            } else if line.starts(with: "jnz") {
                let register = String(parts[1])
                let jump = Int(parts[2])!
                let instruction = Instruction.jnz(register, jump)
                instructions.append(instruction)
            } else {
                fatalError()
            }
        }
        return instructions
    }
}


class Computer {
    private var pointer = 0
    private(set) var registers = [
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    ]
    private var instructions: [Instruction] = []


    func load(instructions: [Instruction]) {
        self.instructions = instructions
        pointer = 0
        setRegisters(a: 0, b: 0, c: 0, d: 0)
    }


    func run() {
        let maxPointer = instructions.count
        while true {
            let i = instructions[pointer]

//            print(pointer, i)

            switch i {
            case .cpy(let a, let b):
                cpy(a: a, b: b)
            case .cpyValue(let a, let b):
                cpyValue(a: a, b: b)
            case .inc(let a):
                inc(a: a)
            case .dec(let a):
                dec(a: a)
            case .jnz(let a, let b):
                jnz(a: a, b: b)
            }

            if pointer >= maxPointer {
                break
            }
        }
    }


    func setRegisters(a: Int, b: Int, c: Int, d: Int) {
        registers["a"] = a
        registers["b"] = b
        registers["c"] = c
        registers["d"] = d
    }
}


private extension Computer {
    func cpy(a: Int, b: String) {
        registers[b] = a
        pointer += 1
    }


    func cpyValue(a: String, b: String) {
        registers[b] = registers[a]
        pointer += 1
    }


    func inc(a: String) {
        registers[a]! += 1
        pointer += 1
    }


    func dec(a: String) {
        registers[a]! -= 1
        pointer += 1
    }


    func jnz(a: String, b: Int) {
        if registers[a] != 0 {
            pointer += b
        } else {
            pointer += 1
        }
    }
}
