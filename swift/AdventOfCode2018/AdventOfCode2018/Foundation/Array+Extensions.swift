//
//  Array+Extensions.swift
//  AdventOfCode2018
//
//  Created by gary on 25/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation


extension Array where Element == Coordinate {
    func sortByReadingOrder() -> [Element] {
        return sorted(by: sortCoordinatesByReadingOrder)
    }
}


private func sortCoordinatesByReadingOrder(lhs: Coordinate, rhs: Coordinate) -> Bool {
    if lhs.y < rhs.y {
        return true
    } else if lhs.y == rhs.y {
        return lhs.x < rhs.x
    }
    return false
}
