//
//  Registers.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//


final class Registers {
    private let number: Int
    var values: [Int]

    init(number: Int) {
        self.number = number
        values = Array(repeating: 0, count: number)
    }
}


extension Registers {
    func get(_ r: Int) -> Int {
        return values[r]
    }


    func set(_ r: Int, value: Int) {
        values[r] = value
    }


    func set(_ newValues: Int...) {
        for (i, value) in newValues.enumerated() {
            values[i] = value
        }
    }

    
    func areEqual(_ otherValues: Int...) -> Bool {
        if otherValues.count != values.count { return false }
        for (i, value) in otherValues.enumerated() {
            if values[i] != value { return false}
        }
        return true
    }
}


extension Registers: CustomDebugStringConvertible {
    var debugDescription: String {
        return values.debugDescription
    }
}
