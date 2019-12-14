//
//  GameConsole.swift
//  AdventOfCode2019
//
//  Created by gary on 14/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

protocol GameConsoleDelegate: class {
    func receive(triplet: GameConsole.Triplet, from console: GameConsole)
    func inputRequest(from console: GameConsole)
}


final class GameConsole: Console {
    struct Triplet {
        let x: Int
        let y: Int
        let c: Int
    }

    private weak var delegate: GameConsoleDelegate?
    private var input: [Int] = []
    private var output: [Int] = []
    private var x = 0
    private var y = 0
    private var c = 0
    private var inputPosition = 0

    init() {}


    func read() -> Int {
        delegate?.inputRequest(from: self)
        return input.last!
    }


    func write(_ n: Int) {
        if inputPosition == 0 {
            x = n
            inputPosition += 1
        } else if inputPosition == 1 {
            y = n
            inputPosition += 1
        } else {
            c = n
            inputPosition = 0
            delegate?.receive(triplet: Triplet(x: x, y: y, c: c), from: self)
        }
    }


    func addInput(_ n: Int) {
        input.append(n)
    }


    func getMostRecentOutput() -> Int {
        return output.last!
    }


    func add(delegate: GameConsoleDelegate) {
        self.delegate = delegate
    }
}
