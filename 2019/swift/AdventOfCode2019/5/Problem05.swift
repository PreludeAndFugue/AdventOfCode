//
//  Problem05.swift
//  AdventOfCode2019
//
//  Created by gary on 05/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem05: Problem {
    private let file = "5/data05.txt"
    private lazy var input = self.makeInput()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 5, r1, r2)
    }
}


// MARK: - Private

private extension Problem05 {
    private func makeInput() -> [Int] {
        let string = try! String(contentsOfFile: path + file)
        return string.makeIntegers(separator: ",")
    }


    private func part1() -> Int {
        let console = AutoConsole(input: [1])
        let computer = Computer(memory: input, console: console)
        computer.run()
        return console.output.last!
    }


    private func part2() -> Int {
        let console = AutoConsole(input: [5])
        let computer = Computer(memory: input, console: console)
        computer.run()
        return console.output.last!
    }
}
