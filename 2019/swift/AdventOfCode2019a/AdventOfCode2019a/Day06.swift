//
//  Day06.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

private typealias Map = [String: [String]]
private typealias InvertedMap = [String: String]


func day06() {
    let s = get(file: "06")
//    let s = test2
    let map = makeMap(s: s)

    let p1 = part1(location: "COM", map: map)
    print(p1)

    let p2 = part2(map: map)
    print(p2)
}


private func part1(location: String, map: Map, depth: Int = 1) -> Int {
    let children = map[location, default: []]
    if children.isEmpty {
        return 0
    }
    let n = depth * children.count
    var m = 0
    for child in children {
        m += part1(location: child, map: map, depth: depth + 1)
    }
    return m + n
}


private func part2(map: Map) -> Int {
    let inv = invert(map: map)
    let you = makePath(start: "YOU", map: inv)
    let santa = makePath(start: "SAN", map: inv)

    let santaSet = Set(santa)
    for (i, c) in you.enumerated() {
        if santaSet.contains(c) {
            let j = santa.firstIndex(of: c)!
            return i + j
        }
    }
    fatalError()
}


private func makeMap(s: String) -> Map {
    var map: Map = [:]
    let x = s.trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
    for a in x {
        let parts = a.split(separator: ")")
        let p1 = String(parts[0])
        let p2 = String(parts[1])
        map[p1, default: []].append(p2)
    }
    return map
}


private func invert(map: Map) -> InvertedMap {
    var result: InvertedMap = [:]
    var children: Set<String> = []
    for (k, v) in map {
        for c in v {
            if children.contains(c) {
                fatalError()
            }
            result[c] = k
            children.insert(c)
        }
    }
    return result
}


private func makePath(start: String, map: InvertedMap) -> [String] {
    var result: [String] = []
    var child = start
    while true {
        if let parent = map[child] {
            result.append(parent)
            child = parent
        } else {
            break
        }
    }
    return result
}


private let test1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""


private let test2 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""
