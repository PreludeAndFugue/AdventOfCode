//
//  Runner16Part1.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let pattern = "Before: \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]\n(\\d+) (\\d+) (\\d+) (\\d+)\nAfter:  \\[(\\d+), (\\d+), (\\d+), (\\d+)\\]"
private let pattern1 = "Before: "


final class Runner16Part1 {
    private let re = try! NSRegularExpression(pattern: pattern, options: [])

    func run() {
        var results: [Int: Int] = [:]
        for (i, data) in makeData().enumerated() {
            for opCodeFunc in OpCode.allOpCodeFunctions {
                if isMatch(opCode: opCodeFunc, data: data) {
                    let currentCount = results[i, default: 0]
                    results[i] = currentCount + 1
                }
            }
        }
        var total = 0
        for (_, value) in results {
            if value >= 3 {
                total += 1
            }
        }
        print("total", total)
        print(results)
    }


    func run1() {
        var rawResults: [Int: Set<String>] = [:]
        for data in makeData(){
            for opCodeRawValue in 0...15 {
                let registers = Registers(number: 4)
                registers.set(data.before.0, data.before.1, data.before.2, data.before.3)
                let opCode = OpCode(rawValue: opCodeRawValue, a: data.instruction.1, b: data.instruction.2, c: data.instruction.3)
                opCode.evaluate(registers: registers)
                if registers.areEqual(data.after.0, data.after.1, data.after.2, data.after.3) {
                    if var result = rawResults[data.instruction.0] {
                        result.insert(opCode.debugDescription)
                        rawResults[data.instruction.0] = result
                    } else {
                        rawResults[data.instruction.0] = [opCode.debugDescription]
                    }
                }
            }
        }

        var finalResults: [Int: String] = [:]
        while true {
            guard let (codeInt, codeName) = getUnique(from: rawResults) else { break }
            finalResults[codeInt] = codeName
            rawResults.removeValue(forKey: codeInt)
            for (key, value) in rawResults {
                rawResults[key] = value.subtracting([codeName])
            }
        }
        print(finalResults)
    }
}


// MARK: - Private

private extension Runner16Part1 {
    func makeData() -> [Data16Part1] {
        let range = NSRange(location: 0, length: data16Part1.count)
        var data: [Data16Part1] = []
        for match in re.matches(in: data16Part1, options: [], range: range) {
            let groups = match.groups(for: data16Part1)
            data.append(Data16Part1(data: groups))
        }
        return data
    }


    func isMatch(opCode: (Int, Int, Int, Registers) -> Void, data: Data16Part1) -> Bool {
        let registers = Registers(number: 4)
        registers.set(data.before.0, data.before.1, data.before.2, data.before.3)
        opCode(data.instruction.1, data.instruction.2, data.instruction.3, registers)
        return registers.areEqual(data.after.0, data.after.1, data.after.2, data.after.3)
    }
}


// MARK: - Private part 1

private extension Runner16Part1 {
    func getUnique(from results: [Int: Set<String>]) -> (Int, String)? {
        for (key, value) in results {
            if value.count == 1 {
                return (key, value.first!)
            }
        }
        return nil
    }
}
