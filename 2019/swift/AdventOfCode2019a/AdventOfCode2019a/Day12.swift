//
//  Day12.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation
import RegexBuilder

func day12() {
    let s = get(file: "12")
//    let s = test2.trimmingCharacters(in: .whitespacesAndNewlines)
    let (xs, ys, zs) = parse(s: s)

    let p1 = part1(xs: xs, ys: ys, zs: zs)
    print(p1)

    let p2 = part2(xs: xs, ys: ys, zs: zs)
    print(p2)
}


private func part1(xs: [Int], ys: [Int], zs: [Int]) -> Int {
    var xs = xs
    var ys = ys
    var zs = zs
    var vxs = [0, 0, 0, 0]
    var vys = [0, 0, 0, 0]
    var vzs = [0, 0, 0, 0]

    for _ in 0..<1000 {
        apply(xs: &xs, ys: &ys, zs: &zs, vxs: &vxs, vys: &vys, vzs: &vzs)
    }
    return totalEnergy(xs: xs, ys: ys, zs: zs, vxs: vxs, vys: vys, vzs: vzs)
}


private func part2(xs: [Int], ys: [Int], zs: [Int]) -> Int {
    var xs = xs
    var ys = ys
    var zs = zs
    var vxs = [0, 0, 0, 0]
    var vys = [0, 0, 0, 0]
    var vzs = [0, 0, 0, 0]

    var statesX: Set<[Int]> = []
    var statesY: Set<[Int]> = []
    var statesZ: Set<[Int]> = []

    var statesXPosition: [[Int]: Int] = [:]
    var statesYPosition: [[Int]: Int] = [:]
    var statesZPosition: [[Int]: Int] = [:]

    statesX.insert(xs + vxs)
    statesY.insert(ys + vys)
    statesZ.insert(zs + vzs)

    statesXPosition[xs + vxs] = 0
    statesYPosition[ys + vys] = 0
    statesZPosition[zs + vzs] = 0

    var foundX = false
    var foundY = false
    var foundZ = false

    var ix = 0
    var iy = 0
    var iz = 0

    for i in 1..<1_000_000 {
        apply(xs: &xs, ys: &ys, zs: &zs, vxs: &vxs, vys: &vys, vzs: &vzs)
        if !foundX {
            let x = xs + vxs
            if statesX.contains(x) {
                ix = i
                foundX = true
            } else {
                statesX.insert(x)
                statesXPosition[x] = i
            }
        }
        if !foundY {
            let y = ys + vys
            if statesY.contains(y) {
                iy = i
                foundY = true
            } else {
                statesY.insert(y)
                statesYPosition[y] = i
            }
        }
        if !foundZ {
            let z = zs + vzs
            if statesZ.contains(z) {
                iz = i
                foundZ = true
            } else {
                statesZ.insert(z)
                statesZPosition[z] = i
            }
        }
        if foundX && foundY && foundZ {
            break
        }
    }
    let a = lcm(a: ix, b: iy)
    let b = lcm(a: a, b: iz)
    return b
}


private func apply(xs: inout [Int], ys: inout [Int], zs: inout [Int], vxs: inout [Int], vys: inout [Int], vzs: inout [Int]) {
    // apply gravity
    applyGravityToCoord(cs: xs, vs: &vxs)
    applyGravityToCoord(cs: ys, vs: &vys)
    applyGravityToCoord(cs: zs, vs: &vzs)

    // move
    applyMoveToCoord(cs: &xs, vs: vxs)
    applyMoveToCoord(cs: &ys, vs: vys)
    applyMoveToCoord(cs: &zs, vs: vzs)
}


private func applyGravityToCoord(cs: [Int], vs: inout [Int]) {
    for (i, c) in cs.enumerated() {
        var v = 0
        for otherC in cs {
            if otherC < c {
                v -= 1
            } else if otherC > c {
                v += 1
            }
        }
        vs[i] += v
    }
}


private func applyMoveToCoord(cs: inout [Int], vs: [Int]) {
    for (i, v) in vs.enumerated() {
        cs[i] += v
    }
}


private func totalEnergy(xs: [Int], ys: [Int], zs: [Int], vxs: [Int], vys: [Int], vzs: [Int]) -> Int {
    var totalE = 0
    for i in 0...3 {
        let p = abs(xs[i]) + abs(ys[i]) + abs(zs[i])
        let k = abs(vxs[i]) + abs(vys[i]) + abs(vzs[i])
        let e = p * k
        totalE += e
    }
    return totalE
}


private func parse(s: String) -> ([Int], [Int], [Int]) {
    var xs: [Int] = []
    var ys: [Int] = []
    var zs: [Int] = []
    for line in s.split(separator: "\n") {
        let m = line.wholeMatch(of: regex)!
        let x = Int(m.output.1)!
        let y = Int(m.output.2)!
        let z = Int(m.output.3)!
        xs.append(x)
        ys.append(y)
        zs.append(z)
    }
    return (xs, ys, zs)
}


private let test1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

private let test2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""

private let regex = Regex {
    "<x="
    Capture {
      Regex {
        Optionally {
          "-"
        }
        OneOrMore(.digit)
      }
    }
    ", y="
    Capture {
      Regex {
        Optionally {
          "-"
        }
        OneOrMore(.digit)
      }
    }
    ", z="
    Capture {
      Regex {
        Optionally {
          "-"
        }
        OneOrMore(.digit)
      }
    }
    ">"
  }
  .anchorsMatchLineEndings()
