//
//  Problem07.swift
//  AdventOfCode2019
//
//  Created by gary on 07/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

typealias PhaseSetting = Int
typealias InputSignal = Int
typealias OutputSignal = Int

final class Problem07: Problem {
    private let file = "7/data07.txt"
    private lazy var input = self.makeInput()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(r1, r2)
    }
}


// MARK: - Private-ish

extension Problem07 {
    private func part1() -> Int {
        var maxIntensity = Int.min
        for phases in [0, 1, 2, 3, 4].permutations() {
            let intensity = runComputers(memory: input, phases: phases)
            if intensity > maxIntensity {
                maxIntensity = intensity
            }
        }
        return maxIntensity
    }


    private func part2() -> Int {
        var maxSignal = Int.min
        for phases in [5, 6, 7, 8, 9].permutations() {
            let signal = runFeedbackComputers(memory: input, phases: phases)
            if signal > maxSignal {
                maxSignal = signal
            }
        }
        return maxSignal
    }


    private func makeInput() -> [Int] {
        let string = try! String(contentsOfFile: path + file)
        return string.makeIntegers(separator: ",")
    }


    func runComputer(memory: [Int], phase: PhaseSetting, inputSignal: InputSignal) -> OutputSignal {
        let console = AutoConsole(input: [phase, inputSignal])
        let computer = Computer(memory: memory, console: console)
        computer.run()
        return console.output.last!
    }


    func runComputers(memory: [Int], phases: [PhaseSetting]) -> Int {
        var inputSignal = 0
        for phase in phases {
            inputSignal = runComputer(memory: memory, phase: phase, inputSignal: inputSignal)
        }
        return inputSignal
    }


    func runFeedbackComputers(memory: [Int], phases: [PhaseSetting]) -> Int {
        let computers = makeFeedbackComputers(memory: memory, phases: phases)
        let count = computers.count
        while true {
            for (i, computer) in computers.enumerated() {
                computer.run()
                if i == count - 1 && computer.isFinished {
                    return computer.getMostRecentOutput()
                }
                let nextComputer = computers[(i + 1) % count]
                nextComputer.addInput(computer.getMostRecentOutput())
            }
        }
    }


    func makeFeedbackComputers(memory: [Int], phases: [PhaseSetting]) -> [Computer] {
        var computers: [Computer] = []
        for (i, phase) in phases.enumerated() {
            let input = i == 0 ? [phase, 0] : [phase]
            let console = AutoConsole(input: input)
            let computer = Computer(memory: memory, console: console, runMode: .pauseAtOutput)
            computers.append(computer)
        }
        return computers
    }
}
