//
//  Cell.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation


class Location {
    let coord: Coordinate
    var unit: Unit

    
    init(coord: Coordinate, unit: Unit) {
        self.coord = coord
        self.unit = unit
    }
}


extension Location: Equatable {
    static func == (lhs: Location, rhs: Location) -> Bool {
        return lhs.coord == rhs.coord
    }
}


extension Location: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(coord)
    }
}


extension Location: CustomDebugStringConvertible {
    var debugDescription: String {
        "\(coord): \(unit)"
    }
}
