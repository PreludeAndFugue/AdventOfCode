//
//  Circle.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation


final class Circle {
    private let startNode: Node
    var currentNode: Node

    init(value: Int) {
        self.currentNode = Node(value: value, next: nil, previous: nil)
        self.startNode = currentNode
        currentNode.next = currentNode
        currentNode.previous = currentNode
    }


    func insert(value: Int) {
        let newNode = Node(value: value)
        let afterNode = currentNode.next!
        currentNode.next = newNode
        newNode.previous = currentNode
        newNode.next = afterNode
        afterNode.previous = newNode
        currentNode = newNode
    }


    func remove() -> Node {
        guard
            let previous = currentNode.previous,
            let next = currentNode.next
        else {
            fatalError("Current node doesn't have previous and next nodes")
        }
        previous.next = next
        next.previous = previous
        let oldCurrentNode = currentNode
        currentNode = next
        return oldCurrentNode
    }


    func moveClockwise(n: Int) {
        for _ in 0..<n {
            guard let next = currentNode.next else { return }
            currentNode = next
        }
    }


    func moveAntiClockwise(n: Int) {
        for _ in 0..<n {
            guard let previous = currentNode.previous else { return }
            currentNode = previous
        }
    }
}


extension Circle: CustomDebugStringConvertible {
    var debugDescription: String {
        var values: [Int] = []
        let start = zeroNode

        var node = start
        values.append(node.value)
        while true {
            let next = node.next!
            if next.value == start.value {
                break
            }
            values.append(next.value)
            node = next
        }
        return "\(values)"
    }


    private var zeroNode: Node {
        var node = currentNode
        while true {
            if node.value == 0 {
                return node
            }
            node = node.next!
        }
    }
}
