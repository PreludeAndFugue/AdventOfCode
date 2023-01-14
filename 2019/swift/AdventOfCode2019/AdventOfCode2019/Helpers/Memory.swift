//
//  Memory.swift
//  AdventOfCode2019
//
//  Created by gary on 10/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

struct Memory {
    private var memory: [Int: Int] = [:]

    init(fromArray array: [Int]) {
        for (i, n) in array.enumerated() {
            memory[i] = n
        }
    }

    
    subscript(index: Int) -> Int {
        get {
            return memory[index, default: 0]
        }

        set(newValue) {
            memory[index] = newValue
        }
    }


    var asArray: [Int] {
        let maxPointer = memory.keys.max()!
        var array = Array(repeating: 0, count: maxPointer + 1)
        for (k, v) in memory {
            array[k] = v
        }
        return array
    }
}


extension Memory: Equatable {
    static func == (lhs: [Int], rhs: Memory) -> Bool {
        return lhs == rhs.asArray
    }


    static func == (lhs: Memory, rhs: [Int]) -> Bool {
        return lhs.asArray == rhs
    }
}
