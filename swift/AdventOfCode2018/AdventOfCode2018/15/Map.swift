//
//  Map.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Map {
    private let cells: [[MapCell]]

    init(cells: [[MapCell]]) {
        self.cells = cells
    }


    func getCell(for unit: Unit) -> MapCell? {
        for row in cells {
            for cell in row {
                if case let .unit(testUnit) = cell.type {
                    if testUnit == unit {
                        return cell
                    }
                }
            }
        }
        return nil
    }


    func getCell(at coordinate: Coordinate) -> MapCell {
        return cells[coordinate.y][coordinate.x]
    }


    func getNeighbours(of coordinate: Coordinate) -> [MapCell] {
        let maxX = cells[0].count
        let maxY = cells.count
        var neighbours: [MapCell] = []
        for (dx, dy) in [(0, -1), (-1, 0), (1, 0), (0, 1)] {
            let x = coordinate.x + dx
            let y = coordinate.y + dy
            if x < 0 || y < 0 || x >= maxX || y >= maxY { continue }
            let neighbour = cells[y][x]
            neighbours.append(neighbour)
        }
        return neighbours
    }


    func getEmptyNeighbours(of coordinate: Coordinate) -> [MapCell] {
        return getNeighbours(of: coordinate).filter({ mapCell in
            if case .empty = mapCell.type {
                return true
            } else {
                return false
            }
        })
    }
}


// Map: - CustomDebugStringConvertible

extension Map: CustomDebugStringConvertible {
    var debugDescription: String {
        var cellChrs: [[String]] = []
        for row in cells {
            var rowChrs: [String] = []
            for cell in row {
                rowChrs.append(cell.debugDescription)
            }
            cellChrs.append(rowChrs)
        }
        return cellChrs.map({ $0.joined() }).joined(separator: "\n")
    }
}
