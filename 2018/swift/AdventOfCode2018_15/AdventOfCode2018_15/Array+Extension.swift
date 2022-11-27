//
//  Array+Extension.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation

extension Array where Element == Location {
    mutating func readingOrder() {
        sort(by: { (lhs, rhs) in
            if lhs.coord.y < rhs.coord.y {
                return true
            } else if lhs.coord.y == rhs.coord.y {
                return lhs.coord.x < rhs.coord.x
            } else {
                return false
            }
        })
    }
}


extension Array where Element == BreadthFirstSearch.Path {
    mutating func sort() {
        sort(by: {(lhs: Element, rhs: Element) in
            lhs.length < rhs.length
        })
    }
}
