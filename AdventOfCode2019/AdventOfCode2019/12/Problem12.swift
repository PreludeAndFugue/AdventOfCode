//
//  Problem12.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

private struct CoordState: Hashable {
    let a1: Int
    let a2: Int
    let a3: Int
    let a4: Int
    let a5: Int
    let a6: Int
    let a7: Int
    let a8: Int
}


private struct State {
    struct Part {
        var isDone = false
        var count = 0
        var states: Set<CoordState> = []

        mutating func update(coordState: CoordState) {
            if !isDone {
                if states.contains(coordState) {
                    isDone = true
                } else {
                    count += 1
                    states.insert(coordState)
                }
            }
        }
    }

    var x = Part()
    var y = Part()
    var z = Part()


    var isDone: Bool {
        return x.isDone && y.isDone && z.isDone
    }


    var periods: [Int] {
        return [x.count, y.count, z.count]
    }


    mutating func update(x: CoordState, y: CoordState, z: CoordState) {
        self.x.update(coordState: x)
        self.y.update(coordState: y)
        self.z.update(coordState: z)
    }
}



final class Problem12: Problem {
    private let file = "12/data12.txt"
    private lazy var input: [Moon] = {
        let string = try! String(contentsOfFile: path + file)
        return makeMoons(fromString: string)
    }()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 12, r1, r2)
    }
}


// MARK: - Private

private extension Problem12 {
    private func part1() -> Int {
        let moons = input
        for _ in 0..<1000 {
            step(moons: moons)
        }
        return moons.map({ $0.totalEnergy }).sum()
    }


    private func part2() -> Int {
//        let moons = input
        let moons = makeMoons(fromString: input1)
        var state = State()
        while !state.isDone {
            let coordStates = makeCoordStates(of: moons)
            state.update(x: coordStates.x, y: coordStates.y, z: coordStates.z)
            step(moons: moons)
        }
        return lcm(numbers: state.periods)
    }


    private func step(moons: [Moon]) {
        for pair in moons.combinations(r: 2) {
            let m1 = pair[0]
            let m2 = pair[1]
            applyGravity(moon1: m1, moon2: m2)
        }
        for moon in moons {
            moon.updatePosition()
        }
    }


    private func applyGravity(moon1: Moon, moon2: Moon) {
        let gravity = moon1.getGravity(for: moon2)
        moon1.applyGravity(gravity)
        moon2.applyGravity(-gravity)
    }


    private func makeCoordStates(of moons: [Moon]) -> (x: CoordState, y: CoordState, z: CoordState) {
        let m0 = moons[0]
        let m1 = moons[1]
        let m2 = moons[2]
        let m3 = moons[3]
        return (
            x: CoordState(
                a1: m0.position.x, a2: m1.position.x, a3: m2.position.x, a4: m3.position.x,
                a5: m0.velocity.x, a6: m1.velocity.x, a7: m2.velocity.x, a8: m3.velocity.x
            ),
            y: CoordState(
                a1: m0.position.y, a2: m1.position.y, a3: m2.position.y, a4: m3.position.y,
                a5: m0.velocity.y, a6: m1.velocity.y, a7: m2.velocity.y, a8: m3.velocity.y
            ),
            z: CoordState(
                a1: m0.position.z, a2: m1.position.z, a3: m2.position.z, a4: m3.position.z,
                a5: m0.velocity.z, a6: m1.velocity.z, a7: m2.velocity.z, a8: m3.velocity.z
            )
        )
    }
}


// MARK: - Private input parser

private extension Problem12 {
    private func makeMoons(fromString string: String) -> [Moon] {
        var moons: [Moon] = []
        let regex = try! NSRegularExpression(
            pattern: "<x=(-?\\d+), y=(-?\\d+), z=(-?\\d+)>",
            options: []
        )
        let range = NSRange(location: 0, length: string.utf16.count)
        for match in regex.matches(in: string, options: [], range: range) {
            let x = getInt(from: match.range(at: 1), forString: string)
            let y = getInt(from: match.range(at: 2), forString: string)
            let z = getInt(from: match.range(at: 3), forString: string)
            let coordinate = Coordinate3(x: x, y: y, z: z)
            let moon = Moon(name: "Moon", position: coordinate)
            moons.append(moon)
        }
        return moons
    }


    private func getInt(from nsrange: NSRange, forString string: String) -> Int {
        let startIndex = string.index(string.startIndex, offsetBy: nsrange.lowerBound)
        let endIndex = string.index(string.startIndex, offsetBy: nsrange.upperBound)
        let intString = string[startIndex..<endIndex]
        return Int(String(intString))!
    }
}


private let input1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""


private let input2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""
