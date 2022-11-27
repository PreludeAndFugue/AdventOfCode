//
//  BreadthFirstSearch.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Collections
import Foundation

class BreadthFirstSearch {
    struct Path {
        let length: (Int, Int)
        let locations: [Location]

        func extend(length: (Int, Int), location: Location) -> Path {
            let l0 = self.length.0 + length.0
            let l1 = self.length.1 + length.1
            return Path(length: (l0, l1), locations: locations + [location])
        }
    }


    func search(start: Location, goal: Location, map: Map) -> Path? {
        var seen: Set<Location> = [start]
        var open: Heap<Path> = [Path(length: (0, 0), locations: [start])]
        while !open.isEmpty {
            let path = open.removeMin()
            let end = path.locations.last!
            if end == goal {
                return path
            }
            for (i, n) in map.neighbours(of: end).enumerated() {
                if seen.contains(n) { continue }
                if !n.unit.isEmpty && n != goal { continue }
                seen.insert(n)
                let p = path.extend(length: (1, i), location: n)
                open.insert(p)
            }
        }
        return nil
    }
}


// MARK: - BreadthFirstSearch.Path

extension BreadthFirstSearch.Path: Comparable {
    static func == (lhs: BreadthFirstSearch.Path, rhs: BreadthFirstSearch.Path) -> Bool {
        lhs.length == rhs.length
    }

    static func < (lhs: BreadthFirstSearch.Path, rhs: BreadthFirstSearch.Path) -> Bool {
        lhs.length < rhs.length
    }
}
