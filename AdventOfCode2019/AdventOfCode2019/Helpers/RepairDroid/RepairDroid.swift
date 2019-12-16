//
//  RepairDroid.swift
//  AdventOfCode2019
//
//  Created by gary on 15/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

protocol DroidConsoleDelegate: class {
    func receive(output: RepairDroid.Output, from console: RepairDroid.DroidConsole)
    func inputRequest(from console: RepairDroid.DroidConsole)
}

final class RepairDroid {
    enum Command: Int {
        case north = 1
        case south = 2
        case west = 3
        case east = 4
    }

    enum Output: Int {
        case blocked = 0
        case moved = 1
        case foundOxygenSystem = 2
    }

    private let computer: Computer


    init(memory: [Int], console: DroidConsole) {
        computer = Computer(memory: memory, console: console)
    }


    func run() {
        computer.run()
    }


    func stop() {
        computer.stop()
    }
}


// MARK: - Console

extension RepairDroid {
    class DroidConsole: Console {
        private weak var delegate: DroidConsoleDelegate?
        private var input: [Int] = []
        private var output: [Int] = []


        func add(delegate: DroidConsoleDelegate) {
            self.delegate = delegate
        }


        func read() -> Int {
            delegate?.inputRequest(from: self)
            return input.last!
        }


        func write(_ n: Int) {
            let output = Output(rawValue: n)!
            delegate?.receive(output: output, from: self)
        }


        func addInput(_ n: Int) {
            input.append(n)
        }


        func getMostRecentOutput() -> Int {
            return output.last!
        }


        func add(command: Command) {
            input.append(command.rawValue)
        }
    }
}
