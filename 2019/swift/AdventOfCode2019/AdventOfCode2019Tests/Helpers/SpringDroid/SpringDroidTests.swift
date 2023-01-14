//
//  SpringDroidTests.swift
//  AdventOfCode2019Tests
//
//  Created by gary on 26/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import XCTest
@testable import AdventOfCode2019

private let input = "#####.###########.##.########"


private func mapInput(_ input: String) -> [Bool] {
    input.map({ $0 == "#" ? true : false })
}

private func printHull(_ hull: String, endState: SpringDroid.EndState) {
    let fall: String
    switch endState {
    case .done:
        fall = ""
    case .fall(let position):
        var buffer = Array(repeating: " ", count: position)
        buffer.append("*")
        fall = buffer.joined()
    }
    print("\(input)\n\(fall)")
}


class SpringDroidTests: XCTestCase {
    func testExample() {
        let hull = mapInput(input)
        let droid = SpringDroid(hull: hull)
        let state = droid.run()
        printHull(input, endState: state)
    }
}
