//
//  Program12.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Program12 {
    private let initialState: String
    private var state: String
    private let rules: Rules12
    private var leftPotNo = 0

    private var isFinalState = false
    private let finalState = "#.......#..........#....#....#....#....#.......#....#....#....#.......#......#....#.....#....#....#.......#....#....#........#......#....#....#....#....#"

    init(data: Data12Protocol) {
        self.initialState = data.initialState
        self.state = data.initialState
        self.rules = data.makeRules(data.rules)
        expandState()
    }
}


// MARK: - Public API

extension Program12 {
    func run(generations: Int) {
        print(state)
        for i in 1...generations {
            if isFinalState {
                leftPotNo += (generations - i + 1)
                break
            } else if simplifiedState == finalState {
                isFinalState = true
                leftPotNo += 1
            } else {
                next()
            }
//            print(i, addPotNos())
        }
        print(leftPotNo)
        print(addPotNos())
    }


    func next() {
        var newState = state
        for i in 0...(state.count - 5) {
            let firstIndex = state.index(state.startIndex, offsetBy: i)
            let lastIndex = state.index(state.startIndex, offsetBy: i + 5)
            let part = String(state[firstIndex..<lastIndex])
            let replaceIndex = state.index(firstIndex, offsetBy: 2)
            let replaceIndexEnd = state.index(after: replaceIndex)
            let replacement = rules.map(input: part)
            let range = Range.init(uncheckedBounds: (replaceIndex, replaceIndexEnd))
            newState.replaceSubrange(range, with: replacement)
//            print(i, part, "=>", replacement, "[", state[replaceIndex], "=>", replacement, "]")
        }
//        print(newState)
        print(leftPotNo)
        print(simplifiedState)
        state = newState
        expandState()
    }


    func addPotNos() -> Int {
        var total = 0
        for (i, chr) in state.enumerated() {
            if chr == "#" {
                total += leftPotNo + i
            }
        }
        return total
    }
}


// MARK: - Private

private extension Program12 {
    /**
     Make sure that the state always has two empty pots and the beginning and end
    */
    func expandState() {
        while state[..<state.index(state.startIndex, offsetBy: 3)] != "..." {
            state = "." + state
            leftPotNo -= 1
        }
        while state[state.index(state.endIndex, offsetBy: -3)...] != "..." {
            state = state + "."
        }
    }


    func isEmpty(pots: String) -> Bool {
        return pots == ".."
    }


    var simplifiedState: String {
        let firstIndex = state.firstIndex(of: "#")!
        let lastIndex = state.lastIndex(of: "#")!
        return String(state[firstIndex...lastIndex])
    }
}
