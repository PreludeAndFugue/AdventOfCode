//
//  Unit.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Unit: HasCoordinate {
    enum UnitType: String {
        case elf = "E"
        case goblin = "G"

        var name: String {
            switch self {
            case .elf: return "Elf"
            case .goblin: return "Goblin"
            }
        }
    }


    var coordinate: Coordinate
    let type: UnitType
    var hitPoints: Int
    let attackPower: Int

    init(coordinate: Coordinate, type: UnitType) {
        self.coordinate = coordinate
        self.type = type
        self.hitPoints = 200
        self.attackPower = 3
    }


    var isAlive: Bool {
        return hitPoints > 0
    }


    var typeId: String {
        return type.rawValue
    }


    func attack(_ unit: Unit) {
        unit.hitPoints -= attackPower
    }
}


// MARK: - Hashable

extension Unit: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(coordinate)
        hasher.combine(type)
        hasher.combine(hitPoints)
        hasher.combine(attackPower)
    }
}


// MARK: - Equatable

extension Unit: Equatable {
    static func == (lhs: Unit, rhs: Unit) -> Bool {
        return lhs.coordinate == rhs.coordinate && lhs.type == rhs.type && lhs.hitPoints == rhs.hitPoints && lhs.attackPower == rhs.attackPower
    }
}


extension Unit: CustomDebugStringConvertible {
    var debugDescription: String {
        return "\(type.name)(points: \(hitPoints), coord: \(coordinate))"
    }
}
