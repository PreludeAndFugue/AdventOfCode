//
//  Computer.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

typealias IntCode = Array<Int>

class Computer {
    enum State {
        case running
        case paused
        case done
    }


    enum Instruction {
        enum Mode: Int {
            case position = 0
            case immediate = 1
            case relative = 2
        }

        case adds(Mode, Mode, Mode)
        case multiplies(Mode, Mode, Mode)
        case input(Mode)
        case output(Mode)
        case jumpIfTrue(Mode, Mode)
        case jumpIfFalse(Mode, Mode)
        case lessThan(Mode, Mode, Mode)
        case equals(Mode, Mode, Mode)
        case adjustRelativeBase(Mode)
        case halt
    }


    private(set) var memory: Memory = Memory(program: [])
    private var pointer = 0
    private var relativeBase = 0

    var input: [Int] = []
    var output: [Int] = []
    var state: State = .paused


    func load(program: IntCode) {
        self.memory = Memory(program: program)
        self.pointer = 0
        self.relativeBase = 0
        self.input = []
        self.output = []
    }


    func run() {
        state = .running
        while state == .running {
            switch Instruction(n: memory[pointer]) {
            case .adds(let m1, let m2, let m3):
                adds(mode1: m1, mode2: m2, mode3: m3)
            case .multiplies(let m1, let m2, let m3):
                multiplies(mode1: m1, mode2: m2, mode3: m3)
            case .input(let m1):
                let i = input.removeFirst()
                input_(mode1: m1, input: i)
            case .output(let m1):
                let o = output_(mode1: m1)
                output.append(o)
                state = .paused
            case .jumpIfTrue(let m1, let m2):
                jumpIfTrue(mode1: m1, mode2: m2)
            case .jumpIfFalse(let m1, let m2):
                jumpIfFalse(mode1: m1, mode2: m2)
            case .lessThan(let m1, let m2, let m3):
                lessThan(mode1: m1, mode2: m2, mode3: m3)
            case .equals(let m1, let m2, let m3):
                equals(mode1: m1, mode2: m2, mode3: m3)
            case .adjustRelativeBase(let m1):
                adjustRelativeBase(mode: m1)
            case .halt:
                state = .done
                return
            }
        }
    }
}


// MARK: - Private

private extension Computer {
    func adds(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        let p = mode3 == .relative ? relativeBase + p3 : p3
        memory[p] = n1 + n2
        pointer += 4
    }


    func multiplies(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        let p = mode3 == .relative ? relativeBase + p3 : p3
        memory[p] = n1 * n2
        pointer += 4
    }


    func input_(mode1: Instruction.Mode, input: Int) {
        assert(mode1 != .immediate)
        let p1 = memory[pointer + 1]
        let p = mode1 == .relative ? relativeBase + p1 : p1
        memory[p] = input
        pointer += 2
    }


    func output_(mode1: Instruction.Mode) -> Int {
        let p1 = memory[pointer + 1]
        let n1 = get(p: p1, mode: mode1)
        pointer += 2
        return n1
    }


    func jumpIfTrue(mode1: Instruction.Mode, mode2: Instruction.Mode) {
        let (p1, p2) = get2()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        pointer = n1 != 0 ? n2 : pointer + 3
    }


    func jumpIfFalse(mode1: Instruction.Mode, mode2: Instruction.Mode) {
        let (p1, p2) = get2()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        pointer = n1 == 0 ? n2 : pointer + 3
    }


    func lessThan(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        let p = mode3 == .relative ? relativeBase + p3 : p3
        memory[p] = n1 < n2 ? 1 : 0
        pointer += 4
    }


    func equals(mode1: Instruction.Mode, mode2: Instruction.Mode, mode3: Instruction.Mode) {
        let (p1, p2, p3) = get3()
        let (n1, n2) = get(p1: p1, m1: mode1, p2: p2, m2: mode2)
        let p = mode3 == .relative ? relativeBase + p3 : p3
        memory[p] = n1 == n2 ? 1 : 0
        pointer += 4
    }


    func adjustRelativeBase(mode: Instruction.Mode) {
        let p = memory[pointer + 1]
        let n = get(p: p, mode: mode)
        relativeBase += n
        pointer += 2
    }


    func get2() -> (Int, Int) {
        (memory[pointer + 1], memory[pointer + 2])
    }


    func get3() -> (Int, Int, Int) {
        (memory[pointer + 1], memory[pointer + 2], memory[pointer + 3])
    }


    func get(p1: Int, m1: Instruction.Mode, p2: Int, m2: Instruction.Mode) -> (Int, Int) {
        return (get(p: p1, mode: m1), get(p: p2, mode: m2))
    }


    func get(p: Int, mode: Instruction.Mode) -> Int {
        switch mode {
        case .immediate:
            return p
        case .position:
            return memory[p]
        case .relative:
            return memory[relativeBase + p]
        }
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
        case 9:
            self = .adjustRelativeBase(mode(n, 100))
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
