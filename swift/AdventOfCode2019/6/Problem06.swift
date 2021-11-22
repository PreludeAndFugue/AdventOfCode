//
//  Problem06.swift
//  AdventOfCode2019
//
//  Created by gary on 07/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem06: Problem {
    private let file = "6/data06.txt"
    private lazy var input = self.makeInput()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 6, r1, r2)
    }
}


// MARK: - Private

private extension Problem06 {
    private func part1() -> Int {
        let graph = makeGraphForPart1(from: input)
        return traverseGraph(graph, start: "COM")
    }


    private func part2() -> Int {
        let graph = makeGraphForPart2(from: input)
        let youPath = pathToCOM(from: "YOU", graph: graph)
        let sanPath = pathToCOM(from: "SAN", graph: graph)
        let commonParent = findCommonParent(path1: youPath, path2: sanPath)
        let youDistance = youPath.firstIndex(of: commonParent)! - 1
        let sanDistance = sanPath.firstIndex(of: commonParent)! - 1
        return youDistance + sanDistance
    }


    private func makeInput() -> [Pair] {
        return try! String(contentsOfFile: path + file)
            .trimmingCharacters(in: .newlines)
            .components(separatedBy: "\n")
            .map({ $0.components(separatedBy: ")") })
            .map({ Pair(pair: $0) })
    }
}


// MARK: - Part 1

private extension Problem06 {
    private func makeGraphForPart1(from pairs: [Pair]) -> [String: [String]] {
        var graph: [String: [String]] = [:]
        for pair in pairs {
            graph[pair.planet, default: []].append(pair.satellite)
        }
        return graph
    }


    private func traverseGraph(_ graph: [String: [String]], start: String) -> Int {
        var seen: [Node] = []
        var todo: [Node] = [Node(name: start, distance: 0)]
        while !todo.isEmpty {
            guard let node = todo.popLast() else { continue }
            for name in graph[node.name, default: []] {
                let childNode = Node(name: name, distance: node.distance + 1)
                todo.append(childNode)
            }
            seen.append(node)
        }
        return seen.map({ $0.distance }).sum()
    }
}


// MARK: - Part 2

private extension Problem06 {
    private func makeGraphForPart2(from pairs: [Pair]) -> [String: String] {
        var graph: [String: String] = [:]
        for pair in pairs {
            assert(!graph.contains(where: { $0.key == pair.satellite }))
            graph[pair.satellite] = pair.planet
        }
        return graph
    }


    private func pathToCOM(from satellite: String, graph: [String: String]) -> [String] {
        var path: [String] = [satellite]
        var currentSatellite = satellite
        while true {
            if let planet = graph[currentSatellite] {
                path.append(planet)
                currentSatellite = planet
            } else {
                break
            }
        }
        assert(path.last == "COM")
        assert(path.count == Set(path).count)
        return path
    }


    private func findCommonParent(path1: [String], path2: [String]) -> String {
        for x in path1 {
            if path2.contains(where: { $0 == x }) {
                return x
            }
        }
        fatalError("No common parent")
    }
}


// MARK: - Pair

private struct Pair: CustomDebugStringConvertible {
    let planet: String
    let satellite: String

    init(pair: [String]) {
        assert(pair.count == 2)
        planet = pair[0]
        satellite = pair[1]
    }

    var debugDescription: String {
        return "Pair(\(planet), \(satellite))"
    }
}


// MARK: - Node

private struct Node {
    let name: String
    let distance: Int
}


// MARK: - Test input

private var input1: [Pair] {
    return TEST.components(separatedBy: "\n")
        .filter({ !$0.isEmpty })
        .map({ $0.components(separatedBy: ")") })
        .map({ Pair(pair: $0) })
}


let TEST = """
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
