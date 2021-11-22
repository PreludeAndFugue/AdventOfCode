//
//  Game15.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Game15 {
    private let mapParser = MapParser()
    let map: Map
    private let units: [Unit]


    init(mapString: String) {
        let (units, map) = mapParser.parse(mapString: mapString)
        self.units = units
        self.map = map
    }


    func run() {
        var i = 1
        while true {
            print()
            print("round", i)
            let isRoundComplete = round()
            if !isRoundComplete {
                print("round is incomplete")
                i -= 1
                break
            }
            i += 1
            print(map)
//            printUnitHitPoints()
        }
        print("done")
        print("final score", i, finalScore())
    }
}


// MARK: - Private

private extension Game15 {
    func round() -> Bool {
        for unit in sort(items: units) {

            if case .elf = unit.type {
                print("ignore elf")
                continue
            }

            if !unit.isAlive { continue }
            let targets = getTargets(for: unit)
            if targets.isEmpty { return false }
            if let targetInRange = getInRange(for: unit, from: targets) {
                unit.attack(targetInRange)
                removeIfDead(targetInRange)
            } else if let nextCoord = getOpenInRange(for: unit, from: targets) {
                move(unit: unit, to: nextCoord)
                if let targetInRange = getInRange(for: unit, from: targets) {
                    unit.attack(targetInRange)
                    removeIfDead(targetInRange)
                }
            }
        }
        return true
    }
}


// MARK: - Targets

private extension Game15 {
    func getTargets(for unit: Unit) -> [Unit] {
        let x = units.filter({ $0.type != unit.type }).filter({ $0.isAlive })
//        print("targets for unit", unit, x)
        return x
    }


    func getInRange(for unit: Unit, from targets: [Unit]) -> Unit? {
        let targetsInRange = targets.filter({ $0.coordinate.manhattanDistance(to: unit.coordinate) == 1 })
        var targetsWithMinPoints: [Unit] = []
        var minPoints = Int.max
        for target in targetsInRange {
            if target.hitPoints < minPoints {
                targetsWithMinPoints = [target]
                minPoints = target.hitPoints
            } else if target.hitPoints == minPoints {
                targetsWithMinPoints.append(target)
            }
        }
        return targetsWithMinPoints.sorted(by: sortByReadingOrder).first
    }


    func getOpenInRange(for unit: Unit, from targets: [Unit]) -> Coordinate? {
        var nextCoords: [Coordinate] = []
        var minPathLength = Int.max
        print("path for unit", unit)
        for target in targets {
            let aStar = AStar(map: map)
            let path = aStar.run(start: unit.coordinate, goal: target.coordinate)
            print(path)
            if path.isEmpty { continue }
            if path.count < minPathLength {
                nextCoords = [path.reversed()[1]]
                minPathLength = path.count
            } else if path.count == minPathLength {
                nextCoords.append(path.reversed()[1])
            }
        }
        print("next coords", nextCoords)
        return nextCoords.sortByReadingOrder().first
    }


    func move(unit: Unit, to coordinate: Coordinate) {
        let currentCell = map.getCell(at: unit.coordinate)
        let newCell = map.getCell(at: coordinate)
        unit.coordinate = coordinate
        currentCell.type = .empty
        newCell.type = .unit(unit)
    }


    func removeIfDead(_ target: Unit) {
        if target.isAlive { return }
        let cell = map.getCell(at: target.coordinate)
        cell.type = .empty
    }


    func finalScore() -> Int {
        return units.filter({ $0.isAlive }).map({ $0.hitPoints }).reduce(0, +)
    }


    func printUnitHitPoints() {
        for unit in units.filter({ $0.isAlive }).sorted(by: sortByReadingOrder) {
            print(unit)
        }
    }
}


// MARK: - Sorting

private extension Game15 {
    func sort<T: HasCoordinate>(items: [T]) -> [T] {
        return items.sorted(by: sortByReadingOrder)
    }
}
