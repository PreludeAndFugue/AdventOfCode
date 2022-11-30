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


fileprivate extension String {
    struct Gen {
        static let th = "thGen"
        static let pl = "plGen"
        static let st = "stGen"
        static let pr = "prGen"
        static let ru = "ruGen"
    }
    struct Mic {
        static let th = "thMic"
        static let pl = "plMic"
        static let st = "stMic"
        static let pr = "prMic"
        static let ru = "ruMic"
    }
}


class Day11 {
    struct Node: Comparable {
        static func < (lhs: Day11.Node, rhs: Day11.Node) -> Bool {
            lhs.state.goalDistance < rhs.state.goalDistance
        }

        let state: State
        let count: Int
    }

    struct State: Equatable, Hashable, CustomDebugStringConvertible {
        func hash(into hasher: inout Hasher) {
            hasher.combine(elevator)
            hasher.combine(positions)
        }

        static func == (lhs: Day11.State, rhs: Day11.State) -> Bool {
            lhs.elevator == rhs.elevator && lhs.positions == rhs.positions
        }

        static func < (lhs: Day11.State, rhs: Day11.State) -> Bool {
            lhs.goalDistance < rhs.goalDistance
        }

        let elevator: Int
        let positions: [String: Int]


        init(elevator: Int, thGen: Int, thMc: Int, plGen: Int, plMc: Int, stGen: Int, stMc: Int, prGen: Int, prMc: Int, ruGen: Int, ruMc: Int) {
            self.elevator = elevator
            positions = [
                .Gen.th: thGen, .Mic.th: thMc,
                .Gen.pl: plGen, .Mic.pl: plMc,
                .Gen.st: stGen, .Mic.st: stMc,
                .Gen.pr: prGen, .Mic.pr: prMc,
                .Gen.ru: ruGen, .Mic.ru: ruMc,
            ]
        }

        init(elevator: Int, positions: [String: Int]) {
            self.elevator = elevator
            self.positions = positions
        }

        static let start = State(elevator: 1, thGen: 1, thMc: 1, plGen: 1, plMc: 2, stGen: 1, stMc: 2, prGen: 3, prMc: 3, ruGen: 3, ruMc: 3)
        static let goal = State(elevator: 4, thGen: 4, thMc: 4, plGen: 4, plMc: 4, stGen: 4, stMc: 4, prGen: 4, prMc: 4, ruGen: 4, ruMc: 4)


        var goalDistance: Int {
            40 - positions.values.reduce(0, +)
        }


        var isValid: Bool {
            if positions[.Gen.th] != positions[.Mic.th] {
                let thMc = positions[.Mic.th]
                if positions[.Gen.pl] == thMc || positions[.Gen.st] == thMc || positions[.Gen.pr] == thMc || positions[.Gen.ru] == thMc {
                    return false
                }
            }
            if positions[.Gen.pl] != positions[.Mic.pl] {
                let mic = positions[.Mic.pl]
                if positions[.Gen.th] == mic || positions[.Gen.st] == mic || positions[.Gen.pr] == mic || positions[.Gen.ru] == mic {
                    return false
                }
            }
            if positions[.Gen.st] != positions[.Mic.st] {
                let mic = positions[.Mic.st]
                if positions[.Gen.th] == mic || positions[.Gen.pl] == mic || positions[.Gen.pr] == mic || positions[.Gen.ru] == mic {
                    return false
                }
            }
            if positions[.Gen.pr] != positions[.Mic.pr] {
                let mic = positions[.Mic.pr]
                if positions[.Gen.th] == mic || positions[.Gen.pl] == mic || positions[.Gen.st] == mic || positions[.Gen.ru] == mic {
                    return false
                }
            }
            if positions[.Gen.ru] != positions[.Mic.ru] {
                let mic = positions[.Mic.ru]
                if positions[.Gen.th] == mic || positions[.Gen.pl] == mic || positions[.Gen.st] == mic || positions[.Gen.pr] == mic {
                    return false
                }
            }
            return true
        }


        var debugDescription: String {
            "State(ele: \(elevator), pos: \(positions))"
        }


        func neighbours() -> [State] {
            var results: [State] = []

            let keys = positions.filter({ $0.value == elevator }).keys

//            print("neighbours")
//            print("elevator", elevator)
//            print("keys", keys)

            // Move 1 item
            for key in keys {
//                print("    \(key)")
                if elevator > 1 {
                    // Move down
                    var newPositions = positions
                    newPositions[key]! -= 1
                    let state = State(elevator: elevator - 1, positions: newPositions)
                    results.append(state)
                }
                if elevator < 4 {
                    // Move up
                    var newPositions = positions
                    newPositions[key]! += 1
                    let state = State(elevator: elevator + 1, positions: newPositions)
                    results.append(state)
                }
            }

            // Move 2 items
            if keys.count >= 2 {
                for combo in keys.combinations(ofCount: 2) {
                    let key1 = combo[0]
                    let key2 = combo[1]

//                    print("    \(key1), \(key2)")

                    if elevator > 1 {
                        // Move down
                        var newPositions = positions
                        newPositions[key1]! -= 1
                        newPositions[key2]! -= 1
                        let state = State(elevator: elevator - 1, positions: newPositions)
                        results.append(state)
                    }
                    if elevator < 4 {
                        // Move up
                        var newPositions = positions
                        newPositions[key1]! += 1
                        newPositions[key2]! += 1
                        let state = State(elevator: elevator + 1, positions: newPositions)
                        results.append(state)
                    }
                }
            }


            let filtered = results.filter({ $0.isValid })
//            for f in filtered {
//                print("    \(f)")
//            }
            return filtered
        }
    }


    func search() -> Int {
        var q: Heap<Node> = [Node(state: .start, count: 0)]
        var seen: Set<State> = []


        while !q.isEmpty {
            let n = q.removeMin()

//            print(n)
//            print(n.state.goalDistance)
//            print("valid state", n.state.isValid)
//            print("q count", q.count)
//            _ = readLine()


            if n.state == .goal {
                return n.count
            }

            if seen.contains(n.state) { continue }

            seen.insert(n.state)

            for nState in n.state.neighbours() {
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
