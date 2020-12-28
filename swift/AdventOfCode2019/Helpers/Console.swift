//
//  Console.swift
//  AdventOfCode2019
//
//  Created by gary on 06/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

protocol Console {
    func read() -> Int
    func write(_ n: Int)

    func addInput(_ n: Int)
    func getMostRecentOutput() -> Int
}


struct ManualConsole: Console {
    func read() -> Int {
        print("Input: ", terminator: "")
        guard
            let rawValue = readLine(),
            let value = Int(rawValue)
        else {
            fatalError("Invalid input")
        }
        return value
    }


    func write(_ n: Int) {
        print(n)
    }


    func addInput(_ n: Int) {
        // does nothing
    }


    func getMostRecentOutput() -> Int {
        return 0
    }
}


final class AutoConsole: Console {
    private var input: [Int]
    private var inputPosition = -1
    var output: [Int] = []


    init(input: [Int]) {
        self.input = input
    }


    func read() -> Int {
        inputPosition += 1
        return input[inputPosition]
    }


    func write(_ n: Int) {
        output.append(n)
    }


    func addInput(_ n: Int) {
        input.append(n)
    }


    func getMostRecentOutput() -> Int {
        return output.last!
    }
}
