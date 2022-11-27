//
//  Map.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation

class Map {
    var locations: [Coordinate: Location]


    init(string: String) {
        locations = parse(string: string)
    }


    /// All units in reading order.
    var unitLocations: [Location] {
        var locations = locations.values.filter({ !$0.unit.isEmpty })
        locations.readingOrder()
        return locations
    }


    /// All the neighbours of a location in reading order.
    func neighbours(of location: Location) -> [Location] {
        var result: [Location] = []
        for n in Coordinate.neighbours {
            let c = location.coord + n
            if let l = locations[c] {
                result.append(l)
            }
        }
        return result
    }


    func update(_ location: Location) {
        locations[location.coord] = location
    }


    /// Gets a neighbouring opponent.
    ///
    /// If there is more than one neighbouring opponent, then select the
    /// one with the fewest hit points. If more than one opponent has the
    /// fewest hit points, then select the first in reading order.
    ///
    /// - Parameter location: <#location description#>
    /// - Returns: <#description#>
    func opponent(of location: Location) -> Location? {
        assert(!location.unit.isEmpty)
        var n = neighbours(of: location)
        if location.unit.isElf {
            n = n.filter({ $0.unit.isGoblin })
        } else {
            n = n.filter({ $0.unit.isElf})
        }
        if n.isEmpty { return nil }
        return n.min(by: { $0.unit.hitPoints < $1.unit.hitPoints })
    }
}


private func parse(string: String) -> [Coordinate: Location] {
    let lines = string.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n")

    var map: [Coordinate: Location] = [:]
    for (y, line) in lines.enumerated() {
        for (x, ch) in line.enumerated() {
            let c = Coordinate(x: x, y: y)
            switch ch {
            case "#":
                break
            case ".":
                let l = Location(coord: c, unit: .empty)
                map[c] = l
            case "E":
                let l = Location(coord: c, unit: .elf(200))
                map[c] = l
            case "G":
                let l = Location(coord: c, unit: .goblin(200))
                map[c] = l
            default:
                fatalError()
            }
        }
    }
    return map
}


extension Map: CustomDebugStringConvertible {
    var debugDescription: String {
        let xs = locations.keys.map({ $0.x })
        let ys = locations.keys.map({ $0.y })
        let yMin = ys.min()! - 1
        let yMax = ys.max()! + 1
        let xMin = xs.min()! - 1
        let xMax = xs.max()! + 1
        var rows: [String] = []
        for y in yMin...yMax {
            var row: [String] = []
            for x in xMin...xMax {
                let c = Coordinate(x: x, y: y)
                if let v = locations[c] {
                    row.append(v.unit.ch)
                } else {
                    row.append("#")
                }
            }
            rows.append(row.joined())
        }
        return rows.joined(separator: "\n")
    }
}
