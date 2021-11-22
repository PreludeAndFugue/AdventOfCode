//
//  Problem09.swift
//  AdventOfCode2019
//
//  Created by gary on 09/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem09: Problem {
    private let file = "9/data09.txt"
    private lazy var input = self.makeInput()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 9, r1, r2)
    }
}


// MARK: - Private

private extension Problem09 {
    private func part1() -> Int {
        let console = AutoConsole(input: [1])
        let computer = Computer(memory: input, console: console)
        computer.run()
        return console.output.first!
    }


    private func part2() -> Int {
        let console = AutoConsole(input: [2])
        let computer = Computer(memory: input, console: console)
        computer.run()
        return console.output.first!
    }


    private func makeInput() -> [Int] {
        return try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
    }
}
