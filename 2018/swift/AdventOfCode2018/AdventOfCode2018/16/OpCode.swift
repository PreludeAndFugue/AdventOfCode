//
//  OpCodes.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

enum OpCode {
    // Addition
    case addr(Int, Int, Int)
    case addi(Int, Int, Int)
    // Multiplication
    case mulr(Int, Int, Int)
    case muli(Int, Int, Int)
    // Bitwise and
    case banr(Int, Int, Int)
    case bani(Int, Int, Int)
    // Bitwise or
    case borr(Int, Int, Int)
    case bori(Int, Int, Int)
    // Assignment
    case setr(Int, Int, Int)
    case seti(Int, Int, Int)
    // Greater-than testing
    case gtir(Int, Int, Int)
    case gtri(Int, Int, Int)
    case gtrr(Int, Int, Int)
    // Equality testing
    case eqir(Int, Int, Int)
    case eqri(Int, Int, Int)
    case eqrr(Int, Int, Int)


    init(rawValue: Int, a: Int, b: Int, c: Int) {
        switch rawValue {
        case 1: self = .addr(a, b, c)
        case 13: self = .addi(a, b, c)
        case 15: self = .mulr(a, b, c)
        case 14: self = .muli(a, b, c)
        case 0: self = .banr(a, b, c)
        case 9: self = .bani(a, b, c)
        case 8: self = .borr(a, b, c)
        case 5: self = .bori(a, b, c)
        case 3: self = .setr(a, b, c)
        case 7: self = .seti(a, b, c)
        case 6: self = .gtir(a, b, c)
        case 12: self = .gtri(a, b, c)
        case 4: self = .gtrr(a, b, c)
        case 10: self = .eqir(a, b, c)
        case 2: self = .eqri(a, b, c)
        case 11: self = .eqrr(a, b, c)
        default: fatalError()
        }
    }


    init(name: String, a: Int, b: Int, c: Int) {
        switch name {
        case "addr": self = .addr(a, b, c)
        case "addi": self = .addi(a, b, c)
        case "mulr": self = .mulr(a, b, c)
        case "muli": self = .muli(a, b, c)
        case "banr": self = .banr(a, b, c)
        case "bani": self = .bani(a, b, c)
        case "borr": self = .borr(a, b, c)
        case "bori": self = .bori(a, b, c)
        case "setr": self = .setr(a, b, c)
        case "seti": self = .seti(a, b, c)
        case "gtir": self = .gtir(a, b, c)
        case "gtri": self = .gtri(a, b, c)
        case "gtrr": self = .gtrr(a, b, c)
        case "eqir": self = .eqir(a, b, c)
        case "eqri": self = .eqri(a, b, c)
        case "eqrr": self = .eqrr(a, b, c)
        default: fatalError()
        }
    }
}


extension OpCode {
    func evaluate(registers: Registers) {
        switch self {
        case .addr(let a, let b, let c):
            doAddr(a: a, b: b, c: c, registers: registers)
        case .addi(let a, let b, let c):
            doAddi(a: a, b: b, c: c, registers: registers)
        case .mulr(let a, let b, let c):
            doMulr(a: a, b: b, c: c, registers: registers)
        case .muli(let a, let b, let c):
            doMuli(a: a, b: b, c: c, registers: registers)
        case .banr(let a, let b, let c):
            doBanr(a: a, b: b, c: c, registers: registers)
        case .bani(let a, let b, let c):
            doBani(a: a, b: b, c: c, registers: registers)
        case .borr(let a, let b, let c):
            doBorr(a: a, b: b, c: c, registers: registers)
        case .bori(let a, let b, let c):
            doBori(a: a, b: b, c: c, registers: registers)
        case .setr(let a, let b, let c):
            doSetr(a: a, b: b, c: c, registers: registers)
        case .seti(let a, let b, let c):
            doSeti(a: a, b: b, c: c, registers: registers)
        case .gtir(let a, let b, let c):
            doGtir(a: a, b: b, c: c, registers: registers)
        case .gtri(let a, let b, let c):
            doGtri(a: a, b: b, c: c, registers: registers)
        case .gtrr(let a, let b, let c):
            doGtrr(a: a, b: b, c: c, registers: registers)
        case .eqir(let a, let b, let c):
            doEqir(a: a, b: b, c: c, registers: registers)
        case .eqri(let a, let b, let c):
            doEqri(a: a, b: b, c: c, registers: registers)
        case .eqrr(let a, let b, let c):
            doEqrr(a: a, b: b, c: c, registers: registers)
        }
    }
}



extension OpCode {
    static var allOpCodeFunctions: [(Int, Int, Int, Registers) -> Void] {
        return [
            doAddr, doAddi, doMulr, doMuli, doBanr, doBani, doBorr, doBori,
            doSetr, doSeti, doGtir, doGtri, doGtrr, doEqir, doEqri, doEqrr
        ]
    }
}


extension OpCode: CustomDebugStringConvertible {
    var debugDescription: String {
        switch self {
        case .addi(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .addr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .muli(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .mulr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .bani(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .banr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .bori(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .borr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .seti(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .setr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .gtir(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .gtri(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .gtrr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .eqir(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .eqri(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        case .eqrr(let a, let b, let c):
            return "\(name)(\(a), \(b), \(c))"
        }
    }


    private var name: String {
        switch self {
        case .addi: return "addi"
        case .addr: return "addr"
        case .muli: return "muli"
        case .mulr: return "mulr"
        case .bani: return "bani"
        case .banr: return "banr"
        case .bori: return "bori"
        case .borr: return "borr"
        case .seti: return "seti"
        case .setr: return "setr"
        case .gtir: return "gtir"
        case .gtri: return "gtri"
        case .gtrr: return "gtrr"
        case .eqir: return "eqir"
        case .eqri: return "eqri"
        case .eqrr: return "eqrr"
        }
    }
}


extension OpCode: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(name)
    }
}



private func doAddr(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) + registers.get(b))
}

private func doAddi(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) + b)
}

private func doMulr(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) * registers.get(b))
}

private func doMuli(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) * b)
}

private func doBanr(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) & registers.get(b))
}

private func doBani(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) & b)
}

private func doBorr(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) | registers.get(b))
}

private func doBori(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a) | b)
}

private func doSetr(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: registers.get(a))
}

private func doSeti(a: Int, b: Int, c: Int, registers: Registers) {
    registers.set(c, value: a)
}

private func doGtir(a: Int, b: Int, c: Int, registers: Registers) {
    let result = a > registers.get(b) ? 1 : 0
    registers.set(c, value: result)
}

private func doGtri(a: Int, b: Int, c: Int, registers: Registers) {
    let result = registers.get(a) > b ? 1 : 0
    registers.set(c, value: result)
}

private func doGtrr(a: Int, b: Int, c: Int, registers: Registers) {
    let result = registers.get(a) > registers.get(b) ? 1 : 0
    registers.set(c, value: result)
}

private func doEqir(a: Int, b: Int, c: Int, registers: Registers) {
    let result = a == registers.get(b) ? 1 : 0
    registers.set(c, value: result)
}

private func doEqri(a: Int, b: Int, c: Int, registers: Registers) {
    let result = registers.get(a) == b ? 1 : 0
    registers.set(c, value: result)
}

private func doEqrr(a: Int, b: Int, c: Int, registers: Registers) {
    let result = registers.get(a) == registers.get(b) ? 1 : 0
    registers.set(c, value: result)
}
