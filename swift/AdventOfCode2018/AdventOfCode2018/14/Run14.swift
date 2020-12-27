//
//  Run14.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let length = 793061
private let string = "793061"

private let tests: [(Int, String)] = [
    (9, "5158916779"),
    (5, "0124515891"),
    (18, "9251071085"),
    (2018, "5941429882")
]


private let tests2: [(String, Int)] = [
    ("51589", 9),
    ("01245", 5),
    ("92510", 18),
    ("59414", 2018)
]

func run14() {
//    main()
//    test()
    main2()
//    test2()
}


private func main() {
    let runner = Runner14()
    print("part 1", runner.run(length: length))
}


private func main2() {
    let runner = Runner14()
    print(runner.run2(string: string))
}


private func test() {
    for (length, result) in tests {
        let runner = Runner14()
        let testResult = runner.run(length: length)
        print(length, result, testResult)

        assert(testResult == result, "Fail for: \(length)")
    }
}


private func test2() {
    for (string, position) in tests2 {
        let runner = Runner14()
        let testPosition = runner.run2(string: string)
        print(string, position, testPosition)
        assert(testPosition == position, "Fail for: \(string)")
    }
}
