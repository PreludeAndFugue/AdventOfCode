//
//  Memory.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

class Memory {
    private var memory: [Int: Int]

    init(program: IntCode) {
        var mem: [Int: Int] = [:]
        for (i, n) in program.enumerated() {
            mem[i] = n
        }
        self.memory = mem
    }


    subscript(index: Int) -> Int {
        get {
            memory[index]!
        }

        set(newValue) {
            memory[index] = newValue
        }
    }
}
