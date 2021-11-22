//
//  MapCell.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class MapCell: HasCoordinate {
    enum MapCellType {
        case wall
        case empty
        case unit(Unit)
    }

    var type: MapCellType
    var coordinate: Coordinate

    
    init(type: MapCellType, coordinate: Coordinate) {
        self.type = type
        self.coordinate = coordinate
    }


    func manhattanDistance(to other: MapCell) -> Int {
        return self.coordinate.manhattanDistance(to: other.coordinate)
    }
}


// MARK: - Hashable

extension MapCell: Hashable {
    func hash(into hasher: inout Hasher) {
//        hasher.combine(type)
        hasher.combine(coordinate)
    }
}


// MARK: - Equatable

extension MapCell: Equatable {
    static func == (lhs: MapCell, rhs: MapCell) -> Bool {
        return lhs.coordinate == rhs.coordinate
    }
}


// MARK: - CustomDebugStringConvertible

extension MapCell: CustomDebugStringConvertible {
    var debugDescription: String {
        switch type {
        case .wall: return "#"
        case .empty: return "."
        case .unit(let unit): return unit.typeId
        }
    }
}
