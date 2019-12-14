//
//  Problem13.swift
//  AdventOfCode2019
//
//  Created by gary on 14/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem13: Problem {
    private let file = "13/data13.txt"
    private lazy var input: [Int] = {
        try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
    }()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 13, r1, r2)
    }
}


// MARK: - Private

private extension Problem13 {
    private func part1() -> Int {
        let console = AutoConsole(input: [])
        let computer = Computer(memory: input, console: console)
        computer.run()
        let game = Game(data: console.output)
        return game.blockCount
    }


    private func part2() -> Int {
        return 0
    }
}
