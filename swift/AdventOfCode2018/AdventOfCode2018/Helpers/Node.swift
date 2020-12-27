//
//  Node.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Node {
    let value: Int
    var next: Node?
    var previous: Node?

    convenience init(value: Int) {
        self.init(value: value, next: nil, previous: nil)
    }

    init(value: Int, next: Node?, previous: Node?) {
        self.value = value
        self.next = next
        self.previous = previous
    }
}


// MARK: - CustomDebugStringConvertible

extension Node: CustomDebugStringConvertible {
    var debugDescription: String {
        return "Node(v: \(value), p: \(previous?.value), n: \(next?.value))"
    }
}
