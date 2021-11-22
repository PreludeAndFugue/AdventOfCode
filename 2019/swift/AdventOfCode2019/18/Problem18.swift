//
//  Problem18.swift
//  AdventOfCode2019
//
//  Created by gary on 21/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

///
/// First attempt: 4232 - too high
///
/// Second attempt
/// --------------
/// SE(q, mripqjvwufsokecyzgxbna0tdhl, 4276)
/// path 0,0 l,16 y,84 e,168 m,276 z,464 b,494 v,548 r,830 s,930 f,1310 p,1334 h,1386
/// f,1446 t,1908 i,2442 c,2466 w,2514 d,2574 a,2608 g,2632 a,2656 i,2758 t,3292 u,3386
/// t,3480 i,4014 a,4116 x,4174 o,4192 j,4216 n,4238 k,4250 q,4276
///
/// Third attempt (same code)
/// -------------------------
/// SE(q, rizegnxdqpjhuymfbwcovstl0ka, 4232)
/// path 0,0 l,16 e,64 y,148 m,272 b,442 z,472 v,504 r,786 s,886 f,1266 p,1290 h,1342
/// f,1402 t,1864 i,2398 c,2422 w,2470 d,2530 a,2564 g,2588 a,2612 i,2714 t,3248 u,3342
/// t,3436 i,3970 a,4072 x,4130 o,4148 j,4172 n,4194 k,4206 q,4232
///
/// Different results for same input!
///
final class Problem18: Problem {
    private class SearchElement: Equatable, Hashable, CustomDebugStringConvertible {
        let name: String
        let keys: Set<String>
        let distance: Int
        let parent: SearchElement?


        init(name: String, distance: Int, parent: SearchElement?) {
            self.name = name
            if let parent = parent {
                self.keys = parent.keys.union([name])
            } else {
                self.keys = Set([name])
            }
            self.distance = distance
            self.parent = parent
        }


        static func == (lhs: SearchElement, rhs: SearchElement) -> Bool {
            return lhs.name == rhs.name && lhs.keys == rhs.keys
        }


        func hash(into hasher: inout Hasher) {
            hasher.combine(name)
            hasher.combine(keys)
        }


        var debugDescription: String {
            let keyString = keys.joined()
            return "SE(\(name), \(keyString), \(distance))"
        }
    }


    private let file = "18/data18.txt"
    private lazy var input = { try! String(contentsOfFile: path + file) }()

    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 18, r1, r2)
    }
}


// MARK: - Private

private extension Problem18 {
    private func part1() -> Int {
        let edges = Problem18Helper(mapString: input).makeEdges()
        let allKeys = Set(edges.map({ [$0.key1, $0.key2] }).flatMap({ $0 }))
        print("all keys", allKeys)
        let allNeighbours = makeNeighbours(edges: edges)
        var discovered: Set<SearchElement> = []
        let start = SearchElement(name: "0", distance: 0, parent: nil)
        var queue = [start]
//        for (key, values) in allNeighbours {
//            print(key)
//            print(values)
//        }

        var goals: [SearchElement] = []

        while queue.isNotEmpty {
            let node = queue.removeFirst()
//            print("\n\n")
//            print("next node", node, "current path", makePath(node: node))
            if isGoal(element: node, allKeys: allKeys) {
//                print("done", node)
//                print("is goal", node)
                goals.append(node)
            }
//            print("checking node neighbours for:", node)
            for neighbour in getNeighbours(element: node, neighbours: allNeighbours) {
//                print(neighbour)
                if !discovered.contains(neighbour) {
//                    print("neighbour not in discovered")
                    discovered.insert(neighbour)
                    queue.append(neighbour)
                } else {
//                    print("neighbour in discovered")
                }
            }
        }

        print("goals")
        for goal in goals {
            print(goal)
            print("path", makePath(node: goal))
        }

        return 0
    }


    private func isGoal(element: SearchElement, allKeys: Set<String>) -> Bool {
        return element.keys.count == allKeys.count
    }


    private func getNeighbours(element: SearchElement, neighbours: [String: Set<Problem18Helper.Edge>]) -> [SearchElement] {
        var result: [SearchElement] = []
        for n in neighbours[element.name] ?? [] {
            // Don't have all keys to open doors to neighbour
//            print("try to get neighbour", n)
            if !n.doors.isSubset(of: element.keys) { continue }
            let name = n.key1 == element.name ? n.key2 : n.key1
//            if element.keys.contains(name) { continue }
            let newElement = SearchElement(
                name: name,
                distance: element.distance + n.distance,
                parent: element
            )
//            print("got neighbour", newElement)
            result.append(newElement)
        }
        return result.sorted(by: { $0.distance < $1.distance })
    }


    private func makeNeighbours(edges: [Problem18Helper.Edge]) -> [String: Set<Problem18Helper.Edge>] {
        var result: [String: Set<Problem18Helper.Edge>] = [:]
        for edge in edges {
            result[edge.key1, default: Set<Problem18Helper.Edge>()].insert(edge)
            result[edge.key2, default: Set<Problem18Helper.Edge>()].insert(edge)
        }
        return result
    }


    private func makePath(node: SearchElement) -> String {
        var names: [String] = ["\(node.name),\(node.distance)"]
        var item = node.parent
        while item != nil {
            names.append("\(item!.name),\(item!.distance)")
            item = item?.parent
        }
        return names.reversed().joined(separator: " ")
    }
}


private let input1 = """
#########
#b.A.@.a#
#########
"""


private let input2 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""

private let input3 = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
"""

private let input4 = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""

private let input5 = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
"""
