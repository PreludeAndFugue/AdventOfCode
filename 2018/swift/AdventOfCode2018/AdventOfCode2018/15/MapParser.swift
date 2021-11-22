//
//  MapParser.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class MapParser {
    func parse(mapString: String) -> (units: [Unit], map: Map) {
        var cells: [[MapCell]] = []
        var units: [Unit] = []
        for (y, row) in mapString.split(separator: "\n").enumerated() {
            var newRow: [MapCell] = []
            for (x, chr) in row.enumerated() {
                let coordinate = Coordinate(x: x, y: y)
                switch chr {
                case "#":
                    newRow.append(MapCell(type: .wall, coordinate: coordinate))
                case ".":
                    newRow.append(MapCell(type: .empty, coordinate: coordinate))
                case "E":
                    let elf = Unit(coordinate: coordinate, type: .elf)
                    units.append(elf)
                    newRow.append(MapCell(type: .unit(elf), coordinate: coordinate))
                case "G":
                    let goblin = Unit(coordinate: coordinate, type: .goblin)
                    units.append(goblin)
                    newRow.append(MapCell(type: .unit(goblin), coordinate: coordinate))
                default:
                    fatalError()
                }
            }
            cells.append(newRow)
        }
        let map = Map(cells: cells)
        return (units: units, map: map)
    }
}
