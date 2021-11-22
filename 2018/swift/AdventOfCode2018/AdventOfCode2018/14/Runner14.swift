//
//  Runner14.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Runner14 {

    func run(length: Int) -> String {
        var (first, second, last) = makePuzzle14()
        for _ in 0..<(length + 10) {
            (first, second, last) = step(first: first, second: second, last: last)
        }
        return last10(afterN: length, last: last)
    }


    func run2(string: String) -> Int {
        let valueCount = string.count
        var (first, second, last) = makePuzzle14()
        for _ in 0..<23_000_000 {
            (first, second, last) = step(first: first, second: second, last: last)
        }

        print("made nodes")

        var arrayValues: [Int] = []
        var nextNode = last.next!
        while nextNode !== last {
            arrayValues.append(nextNode.value)
            nextNode = nextNode.next!
        }

        let stringValues = arrayValues.map({ String($0) }).joined()
        var firstIndex = stringValues.startIndex
        while true {
            let lastIndex = stringValues.index(firstIndex, offsetBy: valueCount)
            let testString = stringValues[firstIndex..<lastIndex]
            if (testString == string) {
                return firstIndex.encodedOffset
            }
            firstIndex = stringValues.index(after: firstIndex)
        }
    }
}


private extension Runner14 {
    func makePuzzle14() -> (first: Node, second: Node, last: Node) {
        let node1 = Node(value: 3)
        let node2 = Node(value: 7)
        node1.next = node2
        node1.previous = node2
        node2.next = node1
        node2.previous = node1
        return (node1, node2, node2)
    }


    func step(first: Node, second: Node, last: Node) -> (first: Node, second: Node, last: Node) {
        let newFirst = move(node: first)
        let newSecond = move(node: second)
        let total = newFirst.value + newSecond.value
        let values = valuesToInsert(n: total)
        let newLast = insert(ns: values, after: last)
        return (newFirst, newSecond, newLast)
    }


    func move(node: Node) -> Node {
        let steps = 1 + node.value
        var nextNode: Node = node
        for _ in 0..<steps {
            nextNode = nextNode.next!
        }
        return nextNode
    }


    /*
     Insert a new value after the `current` Node as a new Node. This node is returned becaus
     it will be the new last node.
     */
    func insert(n: Int, after current: Node) -> Node {
        let newNode = Node(value: n)
        let nextNode = current.next
        newNode.previous = current
        newNode.next = nextNode
        current.next = newNode
        nextNode?.previous = newNode
        return newNode
    }


    func insert(ns: [Int], after current: Node) -> Node {
        var node = current
        for i in ns {
            node = insert(n: i, after: node)
        }
        return node
    }


    func valuesToInsert(n: Int) -> [Int] {
        if n == 0 { return [0] }
        var values: [Int] = []
        var t = n
        var i = t % 10
        while t != 0 {
            values.append(i)
            t /= 10
            i = t % 10
        }
        return values.reversed()
    }


    func last10(afterN n: Int, last: Node) -> String {
        var node = last.next!
        for _ in 0..<n { node = node.next! }
        var values: [Int] = []
        for _ in 0..<10 {
            values.append(node.value)
            node = node.next!
        }
        return values.map({ String($0) }).joined()
    }


    func lastNValues(n: Int, last: Node) -> String {
        var node = last
        var values: [Int] = []
        for _ in 0..<n {
            values.append(node.value)
            node = node.previous!
        }
        return values.map({ String($0) }).joined()
    }


    func printArray(lastNode: Node) {
        var node = lastNode.next!
        var values: [Int] = [node.value]
        while node !== lastNode {
            node = node.next!
            values.append(node.value)
        }
        print(values)
    }


    func findLength(node: Node) -> Int {
        var total = 1
        var nextNode = node.next!
        while nextNode !== node {
            total += 1
            nextNode = nextNode.next!
        }
        return total
    }
}
