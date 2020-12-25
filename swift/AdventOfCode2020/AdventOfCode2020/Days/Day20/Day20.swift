//
//  Day20.swift
//  AdventOfCode2020
//
//  Created by gary on 22/12/2020.
//

import Foundation

func day20() -> (Int, Int) {
    test1()
    let p1 = part1()
    test2()
    let p2 = part2()
    return (p1, p2)
}


private func parseInput(string: String) -> [Tile] {
    return string.trimmingCharacters(in: .whitespacesAndNewlines)
        .components(separatedBy: "\n\n")
        .map(Tile.init(string:))
}


private func part1() -> Int {
//    let tiles = parseInput(string: String.input(forDay: 20))
//    let neighbourMap = makeNeighourMap(tiles: tiles)
//    let cornerNumbers = neighbourMap.filter({ $0.value.count == 2}).keys
//    return cornerNumbers.product()
    return 0
}


private func part2() -> Int {
    0
}


private func test1() {
    let tiles = parseInput(string: testInput1)
    let neighbourMap = makeNeighourMap(tiles: tiles)
    let cornerNumbers = neighbourMap.filter({ $0.value.count == 2 }).keys
    assert(cornerNumbers.product() == 20_899_048_083_289)
}


private func test2() {
    let tiles = parseInput(string: testInput1)
    let neighbourMap = makeNeighourMap(tiles: tiles)
    let fullImage = FullImage(neighbourMap: neighbourMap)
    print(fullImage.image())
    print()
    print(fullImage.trimmedImage())
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


private let testInput1 = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""
