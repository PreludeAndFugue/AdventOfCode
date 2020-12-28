//
//  Problem11.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem11: Problem {
    private let file = "11/data11.txt"
    private lazy var input: [Int] = {
        try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
    }()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 11, r1, r2)
    }
}


// MARK: - Private

private extension Problem11 {
    private func part1() -> Int {
        let robot = Robot(memory: input, start: .black)
        robot.start()
        return robot.panelsPainted
    }


    private func part2() -> Int {
        let robot = Robot(memory: input, start: .white)
        robot.start()
        print(robot.picture)
        return 0
    }
}
