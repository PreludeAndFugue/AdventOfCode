//
//  Computer.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

typealias IntCode = Array<Int>

class Computer {
    enum Opcode: Int {
        case adds = 1
        case multiplies = 2
        case halt = 99
    }


    private(set) var memory: IntCode = []
    private var pointer = 0


    func load(program: IntCode) {
        self.memory = program
        self.pointer = 0
    }


    func run() {
        while true {
            switch Opcode(rawValue: memory[pointer]) {
            case .adds:
                adds()
            case .multiplies:
                multiplies()
            case .halt:
                return
            case .none:
                fatalError()
            }
        }
    }
}


// MARK: - Private

private extension Computer {
    func adds() {
        let p1 = memory[pointer + 1]
        let p2 = memory[pointer + 2]
        let p3 = memory[pointer + 3]
        let n = memory[p1] + memory[p2]
        memory[p3] = n
        pointer += 4
    }


    func multiplies() {
        let p1 = memory[pointer + 1]
        let p2 = memory[pointer + 2]
        let p3 = memory[pointer + 3]
        let n = memory[p1] * memory[p2]
        memory[p3] = n
        pointer += 4
    }
}
