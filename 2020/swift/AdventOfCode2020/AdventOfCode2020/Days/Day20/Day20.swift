//
//  Day20.swift
//  AdventOfCode2020
//
//  Created by gary on 22/12/2020.
//

import Foundation

func day20() -> (Int, Int) {
    let tiles = parseInput(string: String.input(forDay: 20))
    let neighbourMap = makeNeighourMap(tiles: tiles)

    test1()
    let p1 = part1(neighbourMap: neighbourMap)

    test2()
    let p2 = part2(neighbourMap: neighbourMap)
    return (p1, p2)
}


private func parseInput(string: String) -> [Tile] {
    return string.trimmingCharacters(in: .whitespacesAndNewlines)
        .components(separatedBy: "\n\n")
        .map(Tile.init(string:))
}


private func part1(neighbourMap: [Int: [Tile]]) -> Int {
    let cornerNumbers = neighbourMap.filter({ $0.value.count == 2}).keys
    return cornerNumbers.product()
}


private func part2(neighbourMap: [Int: [Tile]]) -> Int {
    let fullImage = FullImage(neighbourMap: neighbourMap)
    let monster = MonsterRegex()
    var waveCount = 0
    for image in fullImage.trimmedImageAllOrientations(separator: "") {
        let c = monster.count(in: image)
        if c == 0 { continue }
        let hashCount = image.filter({ $0 == "#" }).count
        waveCount = hashCount - c * monster.size
    }
    return waveCount
}


private func test1() {
    let tiles = parseInput(string: Day20.testInput)
    let neighbourMap = makeNeighourMap(tiles: tiles)
    let cornerNumbers = neighbourMap.filter({ $0.value.count == 2 }).keys
    assert(cornerNumbers.product() == 20_899_048_083_289)
}


private func test2() {
    let tiles = parseInput(string: Day20.testInput)
    let neighbourMap = makeNeighourMap(tiles: tiles)
    let fullImage = FullImage(neighbourMap: neighbourMap)
    let monster = MonsterRegex()
    var waveCount = 0
    for image in fullImage.trimmedImageAllOrientations(separator: "") {
        let c = monster.count(in: image)
        if c == 0 { continue }
        let hashCount = image.filter({ $0 == "#" }).count
        waveCount = hashCount - c * monster.size
    }
    assert(waveCount == 273)
}


private func makeNeighourMap(tiles: [Tile]) -> [Int: [Tile]] {
    var map: [Int: [Tile]] = [:]
    var toCheck = [tiles[0]]
    var seen: Set<Int> = []
    while !toCheck.isEmpty {
        let tile = toCheck.removeFirst()
        if seen.contains(tile.n) { continue }
        seen.insert(tile.n)
        let neighbours = getNeighbours(tile: tile, tiles: tiles)
        map[tile.n] = neighbours
        for n in neighbours {
            if seen.contains(n.n) { continue }
            toCheck.append(n)
        }
    }
    return map
}


private func getNeighbours(tile: Tile, tiles: [Tile]) -> [Tile] {
    var neighbours: [Tile] = []
    for other in tiles {
        if other == tile { continue }
        for x in other.allOrientations() {
            if let _ = tile.hasMatchingEdges(with: x) {
                neighbours.append(x)
                break
            }
        }
    }
    return neighbours
}
