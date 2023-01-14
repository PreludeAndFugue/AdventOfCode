//
//  BreadthFirstSearch.swift
//  AdventOfCode2019
//
//  Created by gary on 16/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class BreadthFirstSearch<T: Equatable & Hashable> {
    class Node: Equatable, Hashable, CustomDebugStringConvertible {
        let element: T
        var discovered: Bool
        var parent: Node?

        init(element: T) {
            self.element = element
            self.discovered = false
        }


        var path: [T] {
            var result = [element]
            var node = self
            while true {
                if let parent = node.parent {
                    result.append(parent.element)
                    node = parent
                } else {
                    break
                }
            }
            return result.reversed()
        }


        var debugDescription: String {
            return "N(e: \(element), discovered: \(discovered))"
        }


        func hash(into hasher: inout Hasher) {
            hasher.combine(element)
        }


        static func == (lhs: BreadthFirstSearch.Node, rhs: BreadthFirstSearch.Node) -> Bool {
            return lhs.element == rhs.element
        }
    }


    private class Queue {
        private var nodes: [Node] = []

        var isNotEmpty: Bool {
            return !nodes.isEmpty
        }


        func dequeue() -> Node {
            return nodes.removeFirst()
        }


        func enqueue(_ node: Node) {
            nodes.append(node)
        }
    }


    private let elements: [T]
    private var nodes: [Node]
    private var queue: Queue
    private var neighbours: [Node: [Node]]
    private var getNeighbours: (T, [T]) -> [T]
    private let start: Node
    private let goal: Node


    init(elements: [T], start: T, goal: T, getNeighbours: @escaping (T, [T]) -> [T]) {
        self.elements = elements
        self.nodes = elements.map({ Node(element: $0) })
        self.queue = Queue()
        self.neighbours = [:]
        self.getNeighbours = getNeighbours
        self.start = Node(element: start)
        self.goal = Node(element: goal)
    }


    func run() -> Node {
        start.discovered = true
        queue.enqueue(start)
        while queue.isNotEmpty {
            let node = queue.dequeue()
//            print(node)
            if isGoal(node) {
                return node
            }
            for neighbour in getNeighbourNodes(node) {
//                print("neighbour", neighbour.element)
                if !neighbour.discovered {
                    neighbour.discovered = true
                    neighbour.parent = node
                    queue.enqueue(neighbour)
                }
            }
//            print("\n")
        }
        fatalError()
    }
}


// MARK: - Private

private extension BreadthFirstSearch {
    private func isGoal(_ node: Node) -> Bool {
        return node == goal
    }


    private func getNeighbourNodes(_ node: Node) -> [Node] {
        if let n = neighbours[node] {
            return n
        }
        let m = Set(getNeighbours(node.element, elements))
        let n = nodes.filter({ m.contains($0.element) })
        neighbours[node] = n
        return n
    }
}
