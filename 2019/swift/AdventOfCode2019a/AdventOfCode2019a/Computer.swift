//
//  Computer.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

typealias IntCode = Array<Int>

class Computer {
    enum Instruction {
        enum Mode: Int {
            case position = 0
            case immediate = 1
        }

        case adds(Mode, Mode, Mode)
        case multiplies(Mode, Mode, Mode)
        case input(Mode)
        case output(Mode)
        case jumpIfTrue(Mode, Mode)
        case jumpIfFalse(Mode, Mode)
        case lessThan(Mode, Mode, Mode)
        case equals(Mode, Mode, Mode)
        case halt
    }


    private(set) var memory: IntCode = []
    private var pointer = 0

    var input: [Int] = []
    var output: [Int] = []


    func load(program: IntCode) {
        self.memory = program
        self.pointer = 0
        self.input = []
        self.output = []
    }


    func run() {
        while true {
            switch Instruction(n: memory[pointer]) {
            case .adds(let m1, let m2, let m3):
                adds(mode1: m1, mode2: m2, mode3: m3)
            case .multiplies(let m1, let m2, let m3):
                multiplies(mode1: m1, mode2: m2, mode3: m3)
            case .input(let m1):
                let i = input.popLast()!
                input_(mode1: m1, input: i)
            case .output(let m1):
                let o = output_(mode1: m1)
                output.append(o)
            case .jumpIfTrue(let m1, let m2):
                jumpIfTrue(mode1: m1, mode2: m2)
            case .jumpIfFalse(let m1, let m2):
                jumpIfFalse(mode1: m1, mode2: m2)
            case .lessThan(let m1, let m2, let m3):
                lessThan(mode1: m1, mode2: m2, mode3: m3)
            case .equals(let m1, let m2, let m3):
                equals(mode1: m1, mode2: m2, mode3: m3)
            case .halt:
                return
            }
        }
    }
}


// MARK: - Private

private extension Computer {
    func adds(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        assert(mode3 == .position)
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        let n = n1 + n2
        memory[p3] = n
        pointer += 4
    }


    func multiplies(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        assert(mode3 == .position)
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        let n = n1 * n2
        memory[p3] = n
        pointer += 4
    }


    func input_(mode1: Instruction.Mode, input: Int) {
        assert(mode1 == .position)
        let p1 = memory[pointer + 1]
        memory[p1] = input
        pointer += 2
    }


    func output_(mode1: Instruction.Mode) -> Int {
        let p1 = memory[pointer + 1]
        let n1 = mode1 == .position ? memory[p1] : p1
        pointer += 2
        return n1
    }


    func jumpIfTrue(mode1: Instruction.Mode, mode2: Instruction.Mode) {
        let (p1, p2) = get2()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        if n1 != 0 {
            pointer = n2
        } else {
            pointer += 3
        }
    }


    func jumpIfFalse(mode1: Instruction.Mode, mode2: Instruction.Mode) {
        let (p1, p2) = get2()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        if n1 == 0 {
            pointer = n2
        } else {
            pointer += 3
        }
    }


    func lessThan(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        assert(mode3 == .position)
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        if n1 < n2 {
            memory[p3] = 1
        } else {
            memory[p3] = 0
        }
        pointer += 4
    }


    func equals(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        assert(mode3 == .position)
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)

        if n1 == n2 {
            memory[p3] = 1
        } else {
            memory[p3] = 0
        }
        pointer += 4
    }


    func get2() -> (Int, Int) {
        (memory[pointer + 1], memory[pointer + 2])
    }


    func get3() -> (Int, Int, Int) {
        (memory[pointer + 1], memory[pointer + 2], memory[pointer] + 3)
    }


    func get(p1: Int, m1: Instruction.Mode, p2: Int, m2: Instruction.Mode) -> (Int, Int) {
        let n1 = m1 == .position ? memory[p1] : p1
        let n2 = m2 == .position ? memory[p2] : p2
        return (n1, n2)
    }
}


extension Computer.Instruction {
    init(n: Int) {
        let opcode = n % 100
        switch opcode {
        case 1:
            self = .adds(mode(n, 100), mode(n, 1000), mode(n, 10000))
        case 2:
            self = .multiplies(mode(n, 100), mode(n, 1000), mode(n, 10000))
        case 3:
            self = .input(mode(n, 100))
        case 4:
            self = .output(mode(n, 100))
        case 5:
            self = .jumpIfTrue(mode(n, 100), mode(n, 1000))
        case 6:
            self = .jumpIfFalse(mode(n, 100), mode(n, 1000))
        case 7:
            self = .lessThan(mode(n, 100), mode(n, 1000), mode(n, 10000))
        case 8:
            self = .equals(mode(n, 100), mode(n, 1000), mode(n, 10000))
        case 99:
            self = .halt
        default:
            fatalError()
        }
    }
}


private func mode(_ n: Int, _ d: Int) -> Computer.Instruction.Mode {
    Computer.Instruction.Mode(rawValue: (n / d) % 10)!
}
