//
//  Day09.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

func day09() {
//    let program = test3.trimmingCharacters(in: .whitespacesAndNewlines)
//        .split(separator: ",")
//        .map({ Int($0)! })
    let program = getIncode(file: "09")
    let c = Computer()
    c.load(program: program)
    c.input.append(1)
    c.run()
    print(c.output.first!)

    c.load(program: program)
    c.input.append(2)
    c.run()
    print(c.output.first!)
}


private let test1 = """
109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
"""

private let test2 = """
1102,34915192,34915192,7,4,7,99,0
"""

private let test3 = """
104,1125899906842624,99
"""
