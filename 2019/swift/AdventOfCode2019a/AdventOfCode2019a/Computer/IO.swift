//
//  IO.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation

protocol IO {
    func getInput() -> Int
    func addInput(_ n: Int)

    func setOutput(_ n: Int)
    func getOutput() -> Int

    func reset()
}


class StandardIO: IO {
    private let id: Int

    private var input: [Int] = []
    private var output: [Int] = []

    init(id: Int = 1) {
        self.id = id
    }


    func getInput() -> Int {
        return input.removeFirst()
    }


    func addInput(_ n: Int) {
        input.append(n)
    }


    func getOutput() -> Int {
        return output.removeFirst()
    }


    func setOutput(_ n: Int) {
        output.append(n)
    }


    func reset() {
        input = []
        output = []
    }
}


class GameTestIO: IO {
    private var counter = 0
    private(set) var blockCounter = 0

    
    func setOutput(_ n: Int) {
        if counter % 3 == 2 && n == 2 {
            blockCounter += 1
        }
        counter += 1
    }


    func getInput() -> Int { return 0 }
    func addInput(_ n: Int) {}
    func getOutput() -> Int { return 0 }
    func reset() {}
}


class GameIO: IO {
    private var counter = 0

    private var x = 0
    private var y = 0

    private(set) var score = 0
    private var ball = Point.origin
    private var paddle = Point.origin


    func getInput() -> Int {
        if ball.x < paddle.x {
            return -1
        } else if ball.x > paddle.x {
            return 1
        } else {
            return 0
        }
    }


    func setOutput(_ n: Int) {
        switch counter % 3 {
        case 0:
            x = n
        case 1:
            y = n
        case 2:
            if x == -1 {
                score = n
            } else {
                if n == 3 {
                    paddle = Point(x: x, y: y)
                } else if n == 4 {
                    ball = Point(x: x, y: y)
                }
            }
        default:
            fatalError()
        }
        counter += 1
    }

    
    func addInput(_ n: Int) {}
    func getOutput() -> Int { return 0 }
    func reset() {}
}
