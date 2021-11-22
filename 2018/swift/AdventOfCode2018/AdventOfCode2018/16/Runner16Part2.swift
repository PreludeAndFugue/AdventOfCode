//
//  Runner16Part2.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Runner16Part2 {
    func run() {
        let registers = Registers(number: 4)
        for row in parseData() {
            let opCode = OpCode(rawValue: row.0, a: row.1, b: row.2, c: row.3)
            opCode.evaluate(registers: registers)
        }
        print(registers)
    }
}


// MARK: - Private

private extension Runner16Part2 {
    func parseData() -> [(Int, Int, Int, Int)] {
        var results: [(Int, Int, Int, Int)] = []
        for row in data16Part2.split(separator: "\n") {
            results.append(parse(row: String(row)))
        }
        return results
    }


    private func parse(row: String) -> (Int, Int, Int, Int) {
        let values = row.split(separator: " ").compactMap({ Int($0) })
        return (values[0], values[1], values[2], values[3])
    }
}
