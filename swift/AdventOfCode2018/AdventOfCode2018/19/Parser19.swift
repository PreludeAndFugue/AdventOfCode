//
//  Parser19.swift
//  AdventOfCode2018
//
//  Created by gary on 30/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Parser19 {
    func parse(data: String) -> (Int, [OpCode]) {
        var opCodes: [OpCode] = []
        var pointer: Int = 0
        for (i, line) in data.split(separator: "\n").enumerated() {
            if i == 0 {
                pointer = Int(line.split(separator: " ")[1])!
            } else {
                let instruction = parseInstruction(string: String(line))
                opCodes.append(instruction)
            }
        }
        return (pointer, opCodes)
    }
}


private extension Parser19 {
    func parseInstruction(string: String) -> OpCode {
        let parts = string.split(separator: " ")
        let name = parts[0]
        let values = parts[1...].map({ Int($0)! })
        return OpCode(name: String(name), a: values[0], b: values[1], c: values[2])
    }
}
