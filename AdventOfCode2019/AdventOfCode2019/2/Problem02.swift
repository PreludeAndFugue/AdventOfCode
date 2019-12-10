//
//  Run02.swift
//  AdventOfCode2019
//
//  Created by gary on 03/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem02: Problem {
    private let file = "2/data02.txt"
    private lazy var input = self.makeInput()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 2, r1, r2)
    }
}


// MARK: - Private

private extension Problem02 {
    private func part1() -> Int {
        var memory = input
        memory[1] = 12
        memory[2] = 2

        let computer = Computer(memory: memory, console: ManualConsole())
        computer.run()

        return computer.memory[0]
    }


    private func part2() -> Int {
        let test = 19690720
        for noun in 0...99 {
            for verb in 0...99 {
                let memory = configureMemory(noun: noun, verb: verb)
                let computer = Computer(memory: memory, console: ManualConsole())
                computer.run()
                let result = computer.memory[0]
                if result == test {
                    return 100 * noun + verb
                }
            }
        }
        fatalError()
    }


    private func configureMemory(noun: Int, verb: Int) -> [Int] {
        var memory = input
        memory[1] = noun
        memory[2] = verb
        return memory
    }



    private func makeInput() -> [Int] {
        let string = try! String(contentsOfFile: path + file)
        return string.makeIntegers(separator: ",")
    }
}
