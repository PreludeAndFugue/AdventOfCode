//
//  Run22.swift
//  AdventOfCode2018
//
//  Created by gary on 28/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation
import HeapModule


enum Tool: String {
    case torch
    case climbingGear
    case neither
}


class Map22 {
    enum RegionType: Int {
        case rocky
        case wet
        case narrow

        var description: String {
            switch self {
            case .rocky: return "."
            case .wet: return "="
            case .narrow: return "|"
            }
        }

        var tools: Set<Tool> {
            switch self {
            case .rocky: return [.climbingGear, .torch]
            case .wet: return [.climbingGear, .neither]
            case .narrow: return [.torch, .neither]
            }
        }

        var text: String {
            switch self {
            case .rocky: return "rocky"
            case .wet: return "wet"
            case .narrow: return "narrow"
            }
        }
    }

    private let modulo = 20183
    private let depth: Int
    private let target: Coordinate
    private let targetX: Int
    private let targetY: Int

    private var geologicIndexes: [Coordinate: Int] = [:]
    private var typeCache: [Coordinate: RegionType] = [:]


    init(input: Data22.Input) {
        self.depth = input.depth
        self.target = input.target
        self.targetX = input.target.x
        self.targetY = input.target.y
    }


    func risk() -> Int {
        var total = 0
        for y in 0...target.y {
            for x in 0...target.x {
                let c = Coordinate(x: x, y: y)
                let e = erosionLevel(c)
                total += (e % 3)
            }
        }
        return total
    }


    func draw() -> String {
        var rows: [String] = []
        for y in 0...targetY {
            var row: [String] = []
            for x in 0...targetX {
                let c = Coordinate(x: x, y: y)
                let e = erosionLevel(c)
                let type = RegionType(rawValue: e % 3)!
                row.append(type.description)
            }
            rows.append(row.joined(separator: ""))
        }
        return rows.joined(separator: "\n")
    }


    func type(_ c: Coordinate) -> RegionType {
        if let r = typeCache[c] {
            return r
        }
        let e = erosionLevel(c)
        let type = RegionType(rawValue: e % 3)!
        typeCache[c] = type
        return type
    }


    private func geologicIndex(_ c: Coordinate) -> Int {
        if let n = geologicIndexes[c] {
            return n
        }
        let x = c.x
        let y = c.y
        switch (x, y) {
        case (0, 0), (targetX, targetY):
            return 0
        case (0, _):
            return 48271 * y
        case (_, 0):
            return 16807 * x
        default:
            let c1 = Coordinate(x: x - 1, y: y)
            let c2 = Coordinate(x: x, y: y - 1)
            let n = erosionLevel(c1) * erosionLevel(c2)
            geologicIndexes[c] = n
            return n
        }
    }


    private func erosionLevel(_ c: Coordinate) -> Int {
//        print("erosion level", coord)
        return (geologicIndex(c) + depth) % modulo
    }
}


class Search {
    struct Node: Comparable, CustomDebugStringConvertible {
        static func < (lhs: Search.Node, rhs: Search.Node) -> Bool {
            lhs.minutes < rhs.minutes
        }

        let minutes: Int
        let coord: Coordinate
        let tool: Tool
        let type: Map22.RegionType

        var debugDescription: String {
            "Node(\(minutes), \(coord), \(tool), \(type.text))"
        }
    }

    private let map: Map22
    private let start = Coordinate(x: 0, y: 0)
    private let target: Coordinate


    init(target: Coordinate, map: Map22) {
        self.map = map
        self.target = target
    }


    func search() -> Int {
        var seen: [Coordinate: [Tool: Int]] = [start: [.torch: 0]]
        var q: Heap<Node> = []
        q.insert(Node(minutes: 0, coord: start, tool: .torch, type: .rocky))

        while !q.isEmpty {
            let n = q.removeMin()

//            print(q.count)
//            print(n)
//            _ = readLine()

            if n.coord == target && n.tool == .torch {
                return n.minutes
            }

            // change tool
            let t = otherTool(for: n)
            let n1 = Node(
                minutes: n.minutes + 7,
                coord: n.coord,
                tool: t, type: n.type
            )
            if let mTest = seen[n1.coord]?[n1.tool, default: Int.max] {
                if n1.minutes < mTest {
                    q.insert(n1)
                    seen[n1.coord, default: [:]][n1.tool] = n1.minutes
                }
            } else {
                q.insert(n1)
                seen[n1.coord, default: [:]][n1.tool] = n1.minutes
            }

            // explore neighbours
            let tool = n.tool
            for c in neighbours(of: n.coord) {
                let rt = map.type(c)
                if canMove(to: rt, with: tool) {
                    let n2 = Node(
                        minutes: n.minutes + 1,
                        coord: c,
                        tool: tool,
                        type: rt
                    )

                    if let mTest = seen[n2.coord]?[n2.tool, default: Int.max] {
                        if n2.minutes < mTest {
                            q.insert(n2)
                            seen[n2.coord, default: [:]][n2.tool] = n2.minutes
                        }
                    } else {
                        q.insert(n2)
                        seen[n2.coord, default: [:]][n2.tool] = n2.minutes
                    }
                }
            }
        }

        return Int.max
    }


    private func neighbours(of coord: Coordinate) -> [Coordinate] {
        var coords: [Coordinate] = []
        for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)] {
            let x = coord.x + dx
            let y = coord.y + dy
            if x < 0 || y < 0 {
                continue
            }
            coords.append(Coordinate(x: x, y: y))
        }
        return coords
    }


    private func otherTool(for node: Node) -> Tool {
        node.type.tools.subtracting([node.tool]).first!
    }


    private func canMove(to type: Map22.RegionType, with tool: Tool) -> Bool {
        type.tools.contains(tool)
    }
}


func run22() {
    let input = Data22.input
    let map = Map22(input: input)
//    print(map.risk())

//    print(map.draw())

    let search = Search(target: input.target, map: map)
    let n = search.search()
    print(n)
}
