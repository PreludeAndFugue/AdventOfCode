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
    case jnzInt(Int, String)
    case jnzValue(String, String)
    case tgl(String)
    case skp
    case out(Int)
    case outReg(String)


    var debugDescription: String {
        switch self {
        case .cpy(let a, let b): return "cpy \(a) \(b)"
        case .cpyValue(let a, let b): return "cpy \(a) \(b)"
        case .inc(let a): return "inc \(a)"
        case .dec(let a): return "dec \(a)"
        case .jnz(let a, let b): return "jnz \(a) \(b)"
        case .jnzInt(let a, let b): return "jnz \(a) \(b)"
        case .jnzValue(let a, let b): return "jnz \(a) \(b)"
        case .tgl(let a): return "tgl \(a)"
        case .skp: return "skp"
        case .out(let a): return "out \(a)"
        case .outReg(let a): return "out \(a)"
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
                if register.first?.isLetter == false {
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
                if parts[2].first?.isLetter == false {
                    let jump = Int(parts[2])!
                    let instruction = Instruction.jnz(register, jump)
                    instructions.append(instruction)
                } else {
                    let jump = String(parts[2])
                    let instruction = Instruction.jnzValue(register, jump)
                    instructions.append(instruction)
                }
            } else if line.starts(with: "tgl") {
                let jump = String(parts[1])
                let instruction = Instruction.tgl(jump)
                instructions.append(instruction)
            } else if line.starts(with: "out") {
                let p = parts[1]
                if p.first?.isLetter == false {
                    let instruction = Instruction.out(Int(p)!)
                    instructions.append(instruction)
                } else {
                    let instruction = Instruction.outReg(String(p))
                    instructions.append(instruction)
                }
            } else {
                fatalError()
            }
        }
        return instructions
    }
}


class Computer {
    private var pointer = 0
    private var maxPointer = 0
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
        maxPointer = instructions.count
        setRegisters(a: 0, b: 0, c: 0, d: 0)
    }


    func run() {
        while true {
            let i = instructions[pointer]

//            print(instructions)
//            print(pointer, i)
//            print(i)
//            readLine()

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
            case .jnzInt(let a, let b):
                jnzInt(a: a, b: b)
            case .jnzValue(let a, let b):
                jnzValue(a: a, b: b)
            case .tgl(let a):
                tgl(a: a)
            case .skp:
                skp()
            case .out(let a):
                out(a: "\(a)")
            case .outReg(let a):
                out(a: a)
            }

//            print(registers)
//            print(instructions)
//            print()

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


    func jnzInt(a: Int, b: String) {
        if a != 0 {
            pointer += registers[b]!
        } else {
            pointer += 1
        }
    }


    func jnzValue(a: String, b: String) {
        if registers[a] != 0 {
            pointer += registers[b]!
        } else {
            pointer += 1
        }
    }


    func tgl(a: String) {
        let p = pointer + registers[a]!
        if p < 0 || p >= maxPointer {
            return
        }
        let i = instructions[p]
        switch i {
        case .inc(let a):
            instructions[p] = .dec(a)
        case .dec(let a):
            instructions[p] = .inc(a)
        case .tgl(let a):
            instructions[p] = .inc(a)
        case .jnz(let a, let b):
            instructions[p] = .skp
        case .jnzInt(let a, let b):
            instructions[p] = .cpy(a, b)
        case .jnzValue(let a, let b):
            instructions[p] = .cpyValue(a, b)
        case .cpy(let a, let b):
            instructions[p] = .jnzInt(a, b)
        case .cpyValue(let a, let b):
            instructions[p] = .jnzValue(a, b)
        case .skp:
            break
        case .out, .outReg:
            break
        }
        pointer += 1
    }


    func skp() {
        pointer += 1
    }


    func out(a: String) {
        print(a)
    }
}
