//
//  Problem21.swift
//  AdventOfCode2019
//
//  Created by gary on 25/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem21: Problem {
    private let file = "21/data21.txt"
    private lazy var input = { try! String(contentsOfFile: path + file).makeIntegers(separator: ",") }()

    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 21, r1, r2)
    }
}


// MARK: - Private

private extension Problem21 {
    private func part1() -> Int {
        let program = consoleInput.map({ $0.asciiValue! }).map({ Int($0) })
        let console = AutoConsole(input: program)
        let computer = Computer(memory: input, console: console)
        computer.run()
        let output = readOutput(console.output)
        print(output)
        return 0
    }


    private func readOutput(_ output: [Int]) -> String {
        output.map({ Unicode.Scalar($0)! }).map({ String($0) }).joined()
    }


    private func test(a: Bool, b: Bool, c: Bool, d: Bool) -> Bool {
        func and(x: Bool, y: inout Bool) {
            y = x && y
        }

        func or(x: Bool, y: inout Bool) {
            y = x || y
        }

        func not(x: Bool, y: inout Bool) {
            y = !x
        }

        var t = false
        var j = false

        not(x: a, y: &j)

        return j
    }
}


private let consoleInput = """
NOT A J
WALK

"""
