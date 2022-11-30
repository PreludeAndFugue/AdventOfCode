//
//  Day11.swift
//  AdventOfCode2016
//
//  Created by gary on 29/11/2022.
//

import Algorithms
import Foundation
import HeapModule

// The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
// The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
// The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
// The fourth floor contains nothing relevant.


class Day11 {
    let start = [1, 1, 1, 1, 2, 1, 2, 3, 3, 3, 3]
    let goal = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]


    struct Node: Comparable {
        static func < (lhs: Day11.Node, rhs: Day11.Node) -> Bool {
            lhs.count < rhs.count
        }

        let state: [Int]
        let count: Int
    }


    func goalDistance(_ state: [Int]) -> Int {
        4 * state.count - state.reduce(0, +)
    }


    func isValidState(_ state: [Int]) -> Bool {
        if state[1] != state[2] {
            for i in [3, 5, 7, 9] {
                if state[2] == state[i] {
                    return false
                }
            }
        }
        if state[3] != state[4] {
            for i in [1, 5, 7, 9] {
                if state[4] == state[i] {
                    return false
                }
            }
        }
        if state[5] != state[6] {
            for i in [1, 3, 7, 9] {
                if state[6] == state[i] {
                    return false
                }
            }
        }
        if state[7] != state[8] {
            for i in [1, 3, 5, 9] {
                if state[8] == state[i] {
                    return false
                }
            }
        }
        if state[9] != state[10] {
            for i in [1, 3, 5, 7] {
                if state[10] == state[i] {
                    return false
                }
            }
        }
        return true
    }


    func canMoveDownFrom(_ state: [Int]) -> Bool {
        let elevator = state[0]
        for n in state[1...] {
            if n - elevator < 0 {
                return true
            }
        }
        return false
    }


    func neighbours(_ state: [Int]) -> [[Int]] {
        let elevator = state[0]
        var keys: [Int] = []

        for (i, n) in state[1...].enumerated() {
            if n == elevator {
                keys.append(i + 1)
            }
        }

        let canMoveDown = canMoveDownFrom(state)

        var newStates: [[Int]] = []

        // Move 1
        for key in keys {
            if elevator < 4 {
                // Move up
                var newState = state
                newState[0] += 1
                newState[key] += 1
                if isValidState(newState) {
                    newStates.append(newState)
                }
            }

            if elevator > 1 && canMoveDown {
                // Move down
                var newState = state
                newState[0] -= 1
                newState[key] -= 1
                if isValidState(newState) {
                    newStates.append(newState)
                }
            }
        }

        // Move 2 items

        if keys.count > 1 {
            for pair in keys.combinations(ofCount: 2) {
                if elevator < 4 {
                    var newState = state
                    newState[0] += 1
                    newState[pair[0]] += 1
                    newState[pair[1]] += 1
                    if isValidState(newState) {
                        newStates.append(newState)
                    }
                }

                if elevator > 1 && canMoveDown {
                    var newState = state
                    newState[0] -= 1
                    newState[pair[0]] -= 1
                    newState[pair[1]] -= 1
                    if isValidState(newState) {
                        newStates.append(newState)
                    }
                }
            }
        }
        return newStates
    }


    func search() -> Int {
        var q: Heap<Node> = [Node(state: start, count: 0)]
        var seen: Set<[Int]> = []


        while !q.isEmpty {
            let n = q.removeMin()

//            print(n)
//            print(n.state.goalDistance)
//            print("valid state", n.state.isValid)
//            print("q count", q.count)
//            _ = readLine()


            if n.state == goal {
                return n.count
            }

            for nState in neighbours(n.state) {
                if seen.contains(nState) {
                    continue
                }
                seen.insert(nState)
                q.insert(Node(state: nState, count: n.count + 1))
            }
        }

        return Int.max
    }


    func run() {
        let n = search()
        print(n)
    }
}
