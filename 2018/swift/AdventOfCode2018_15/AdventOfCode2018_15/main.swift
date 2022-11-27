//
//  main.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation


let fm = FileManager()
let url = fm.homeDirectoryForCurrentUser
    .appendingPathComponent("Documents")
    .appendingPathComponent("computing")
    .appendingPathComponent("_AdventOfCode")
    .appendingPathComponent("2018")
    .appendingPathComponent("day15.txt")
let string = try! String(contentsOf: url, encoding: .utf8)

let map = Map(string: string)
let bfs = BreadthFirstSearch()


func findPath(_ location: Location, map: Map) -> BreadthFirstSearch.Path? {
    let uls = map.unitLocations
    let goblinLocations = uls.filter({ $0.unit.isGoblin })
    let elfLocations = uls.filter({ $0.unit.isElf })
    let targets = location.unit.isElf ? goblinLocations : elfLocations
//    print("targets:", targets)
    var paths: [BreadthFirstSearch.Path] = []
    for target in targets {
//        print("    target:", target)
        if let path = bfs.search(start: location, goal: target, map: map) {
//            print("      path", path)
            paths.append(path)
        }
    }
    paths.sort()
    return paths.first
}


func fight(_ location: Location, map: Map) {
    guard let opponent = map.opponent(of: location) else {
        return
    }
//    print("    fight", location, opponent)
//    let attack = location.unit.isElf ? 17 : 3
    let hitPoints = opponent.unit.hitPoints - 3 // - attack
    if hitPoints <= 0 {
        opponent.unit = .empty
        map.update(opponent)
    } else {
        let newUnit = opponent.unit.update(hitPoints: hitPoints)
        opponent.unit = newUnit
        map.update(opponent)
    }
}


func move(_ location: Location, path: BreadthFirstSearch.Path, map: Map) -> Location {
    switch path.length.0 {
    case 0:
        assertionFailure()
        return location
    case 1:
        // Already next to opponent
        return location
    default:
        let newLocation = path.locations[1]
        assert(newLocation.unit.isEmpty)
        let unit = location.unit
        location.unit = .empty
        map.update(location)
        newLocation.unit = unit
        map.update(newLocation)
        return newLocation
    }
}


func part1() {
    print(map)
    let elfCount1 = map.unitLocations.filter({ $0.unit.isElf }).count
    var i = 0
    while true {
        var opponentCount = 0
//        print(i)
        for location in map.unitLocations {
            if location.unit.isEmpty {
                // The unit may have been killed by an opponent.
//                print("Unit has been killed")
                continue
            }
            guard let path = findPath(location, map: map) else {
                continue
            }
            opponentCount += 1
            let newLocation = move(location, path: path, map: map)
            fight(newLocation, map: map)
        }
//        print(map)
        if opponentCount == 0 {
            break
        }
        i += 1
    }

    print()
    print(map)
    for u in map.unitLocations {
        print(u)
    }
    let s = map.unitLocations.map({ $0.unit.hitPoints }).reduce(0, +)
    let elfCount2 = map.unitLocations.filter({ $0.unit.isElf }).count

    print("elf count", elfCount1, elfCount2)

    print(s)
    print(i)
    print(i - 1)
    print(i - 2)

    print(i * s)
    print((i - 1) * s)
    print((i - 2) * s)

}


part1()
