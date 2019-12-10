//
//  Computer.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

final class Computer {
    enum State {
        case idle
        case running
        case paused
        case finished
    }


    enum RunMode {
        case toEnd
        case pauseAtOutput
    }


    enum Opcode: Int {
        case add = 1
        case multiply = 2
        case input = 3
        case output = 4
        case jumpIfTrue = 5
        case jumpIfFalse = 6
        case lessThan = 7
        case equals = 8
        case relativeBaseOffset = 9
        case finish = 99
    }


    enum ParameterMode: Int {
        case position = 0
        case immediate = 1
        case relative = 2
    }


    struct OpcodeData {
        let opcode: Opcode
        let parameterModes: [ParameterMode]
    }


    private var state = State.idle
    private let runMode: RunMode
    private var pointer = 0
    private var relativeBase = 0
    private let debug: Bool
    private let console: Console
    var memory: Memory


    init(memory: [Int], console: Console, runMode: RunMode = .toEnd, debug: Bool = false) {
        self.memory = Memory(fromArray: memory)
        self.console = console
        self.runMode = runMode
        self.debug = debug
    }


    func run() {
        switch state {
        case .idle, .paused, .running:
            state = .running
        case .finished:
            state = .finished
        }
        while state == .running {
            let opcodeData = OpcodeData(memory[pointer])
//            print("pointer, relativeBase", pointer, relativeBase)
//            print(opcodeData)
//            print(memory.asArray)
            switch opcodeData.opcode {
            case .add:
                add(modes: opcodeData.parameterModes)
            case .multiply:
                multiply(modes: opcodeData.parameterModes)
            case .input:
                input(mode: opcodeData.parameterModes[0])
            case .output:
                output(mode: opcodeData.parameterModes[0])
            case .jumpIfTrue:
                jumpIfTrue(modes: opcodeData.parameterModes)
            case .jumpIfFalse:
                jumpIfFalse(modes: opcodeData.parameterModes)
            case .lessThan:
                lessThan(modes: opcodeData.parameterModes)
            case .equals:
                equals(modes: opcodeData.parameterModes)
            case .relativeBaseOffset:
                relativeBaseOffset(mode: opcodeData.parameterModes[0])
            case .finish:
                finish()
            }
        }
    }


    func addInput(_ n: Int) {
        console.addInput(n)
    }


    func getMostRecentOutput() -> Int {
        return console.getMostRecentOutput()
    }


    var isFinished: Bool {
        return state == .finished
    }
}


// MARK: - Private

private extension Computer {
    private func add(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        let m2 = getValue(pointer: pointer + 2, mode: modes[1])
        let p3 = memory[pointer + 3]
        let result = m1 + m2
        memory[p3] = result
        debug(opcode: "add", modes: modes, m1: m1, m2: m2, p3: p3, result: result)
        next(4)
    }


    private func multiply(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        let m2 = getValue(pointer: pointer + 2, mode: modes[1])
        let p3 = memory[pointer + 3]
        let result = m1 * m2
        memory[p3] = result
        debug(opcode: "multiply", modes: modes, m1: m1, m2: m2, p3: p3, result: result)
        next(4)
    }


    private func input(mode: ParameterMode) {
        let value = console.read()
        let p1 = memory[pointer + 1]
        memory[p1 + relativeBase] = value
        debug(opcode: "input", modes: [], m1: 0, m2: 0, p3: 0, result: 0)
        next(2)
    }


    private func output(mode: ParameterMode) {
        let m1 = getValue(pointer: pointer + 1, mode: mode)
        console.write(m1)
        next(2)
        switch runMode {
        case .toEnd:
            // do nothing
            break
        case .pauseAtOutput:
            state = .paused
        }
    }


    private func jumpIfTrue(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        if m1 != 0 {
            pointer = getValue(pointer: pointer + 2, mode: modes[1])
        } else {
            // do nothing except move pointer
            next(3)
        }
    }


    private func jumpIfFalse(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        if m1 == 0 {
            pointer = getValue(pointer: pointer + 2, mode: modes[1])
        } else {
            // do nothing except move pointer
            next(3)
        }
    }


    private func lessThan(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        let m2 = getValue(pointer: pointer + 2, mode: modes[1])
        let m3 = getValue(pointer: pointer + 3, mode: .immediate)
        if m1 < m2 {
            memory[m3] = 1
        } else {
            memory[m3] = 0
        }
        next(4)
    }


    private func equals(modes: [ParameterMode]) {
        let m1 = getValue(pointer: pointer + 1, mode: modes[0])
        let m2 = getValue(pointer: pointer + 2, mode: modes[1])
        let m3 = getValue(pointer: pointer + 3, mode: .immediate)
//        print(pointer + 3, m3, modes[2])
        if m1 == m2 {
            memory[m3] = 1
        } else {
            memory[m3] = 0
        }
        next(4)
    }


    private func relativeBaseOffset(mode: ParameterMode) {
        let m1 = getValue(pointer: pointer + 1, mode: mode)
        relativeBase += m1
//        print("relative-base-offset")
        next(2)
    }


    private func finish() {
        state = .finished
    }


    private func next(_ increment: Int) {
        pointer += increment
    }


    private func getValue(pointer: Int, mode: ParameterMode) -> Int {
        let value = memory[pointer]
        switch  mode {
        case .immediate:
            return value
        case .position:
            return memory[value]
        case .relative:
            return memory[value + relativeBase]
        }
    }


    private func debug(opcode: String, modes: [ParameterMode], m1: Int, m2: Int, p3: Int, result: Int) {
        guard debug else { return }
        print("pointer", pointer)
        print(opcode, m1, ",", m2, ",", p3, "->", result)
        print(modes)
        print(memory)
        print()
    }
}


// MARK: - Computer.Opcode

extension Computer.Opcode {
    var parameterCount: Int {
        switch self {
        case .add:
            return 3
        case .multiply:
            return 3
        case .input:
            return 1
        case .output:
            return 1
        case .jumpIfTrue:
            return 2
        case .jumpIfFalse:
            return 2
        case .lessThan:
            return 3
        case .equals:
            return 3
        case .relativeBaseOffset:
            return 1
        case .finish:
            return 0
        }
    }
}


extension Computer.Opcode: CustomDebugStringConvertible {
    var debugDescription: String {
        switch self {
        case .add: return "add"
        case .equals: return "equals"
        case .finish: return "finish"
        case .input: return "input"
        case .jumpIfFalse: return "jump-if-false"
        case .jumpIfTrue: return "jump-if-true"
        case .lessThan: return "less than"
        case .multiply: return "multiply"
        case .output: return "output"
        case .relativeBaseOffset: return "relative-base-offset"
        }
    }
}


// MARK: - Computer.OpcodeData

extension Computer.OpcodeData {
    init(_ n: Int) {
        let opcodeValue = n % 100
        guard let opcode = Computer.Opcode(rawValue: opcodeValue) else { fatalError() }
        var modeValues = n / 100
        var parameterModes: [Computer.ParameterMode] = []
        for _ in 0..<opcode.parameterCount {
            let value = modeValues % 10
            guard let mode = Computer.ParameterMode(rawValue: value) else { fatalError() }
            parameterModes.append(mode)
            modeValues /= 10
        }
        self.opcode = opcode
        self.parameterModes = parameterModes
    }
}


// MARK: - Computer.ParameterMode

extension Computer.ParameterMode: CustomDebugStringConvertible {
    var debugDescription: String {
        switch self {
        case .immediate:
            return "immediate"
        case .position:
            return "position"
        case .relative:
            return "relative"
        }
    }
}
