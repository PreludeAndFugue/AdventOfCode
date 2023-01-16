//
//  IO.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation

protocol IO {
//    var input: [Int] { get set }
    func getInput() -> Int
    func addInput(_ n: Int)

//    var output: [Int] { get set }
    func setOutput(_ n: Int)
    func getOutput() -> Int

    func reset()
}


class StandardIO: IO {
    private var input: [Int] = []
    private var output: [Int] = []


    func getInput() -> Int {
//        print("io.get", input[0])
        return input.removeFirst()
    }


    func addInput(_ n: Int) {
        input.append(n)
    }


    func getOutput() -> Int {
        output.removeFirst()
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


    func getInput() -> Int { return 0}

    func addInput(_ n: Int) {}

    func setOutput(_ n: Int) {
        if counter % 3 == 2 && n == 2 {
            blockCounter += 1
        }
        counter += 1
    }

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


    func addInput(_ n: Int) {}


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


    func getOutput() -> Int {
        return 0
    }

    func reset() {

    }
}
