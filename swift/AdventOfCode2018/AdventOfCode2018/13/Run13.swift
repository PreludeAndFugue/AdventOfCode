//
//  Run13.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let data = "/Users/gary/Documents/computing/python/adventOfCode/2018/AdventOfCode2018/AdventOfCode2018/13/Data13.txt"
private let testData = "/Users/gary/Documents/computing/python/adventOfCode/2018/AdventOfCode2018/AdventOfCode2018/13/Data13Test.txt"
private let testDataA = "/Users/gary/Documents/computing/python/adventOfCode/2018/AdventOfCode2018/AdventOfCode2018/13/Data13TestA.txt"
private let testDataB = "/Users/gary/Documents/computing/python/adventOfCode/2018/AdventOfCode2018/AdventOfCode2018/13/Data13TestB.txt"
private let testDataC = "/Users/gary/Documents/computing/python/adventOfCode/2018/AdventOfCode2018/AdventOfCode2018/13/Data13TestC.txt"

func run13() {
    main13()
    main13b()
    test13()
    test13b()
    test13c()
}


func main13() {
    let string = try! String(contentsOfFile: data)
    let runner = Runner13(string: string)
    let position = runner.runUntilCrash()
    print(position)
}


func main13b() {
    let string = try! String(contentsOfFile: data)
    let runner = Runner13(string: string)
    let position = runner.runUntilLastCar()
    print(position)
}


func test13() {
    let string = try! String(contentsOfFile: testDataA)
    let runner = Runner13(string: string)
    let position = runner.runUntilCrash()
    let testPosition = Coordinate(x: 7, y: 3)
    print(position)
    assert(position == testPosition)
}


func test13b() {
    let string = try! String(contentsOfFile: testDataB)
    let runner = Runner13(string: string)
    let position = runner.runUntilCrash()
    let testPosition = Coordinate(x: 2, y: 2)
    print(position)
    assert(position == testPosition)
}


func test13c() {
    let string = try! String(contentsOfFile: testDataC)
    let runner = Runner13(string: string)
    let position = runner.runUntilLastCar()
    let testPosition = Coordinate(x: 6, y: 4)
    print(position)
    assert(position == testPosition)
}
