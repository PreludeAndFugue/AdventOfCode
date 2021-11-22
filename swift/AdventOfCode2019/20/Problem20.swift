//
//  Problem20.swift
//  AdventOfCode2019
//
//  Created by gary on 23/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem20: Problem {
    private let file = "20/data20.txt"
    private lazy var data = {
        try! String(contentsOfFile: path + file ).trimmingCharacters(in: .newlines)
    }()

    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 20, r1, r2)
    }
}


// MARK: - Private

private extension Problem20 {
    private func part1() -> Int {
        let (start, end, coords, jumps) = getCoords(from: data)

        func getNeighbours(element: Coordinate, elements: [Coordinate]) -> [Coordinate] {
            var n = Set(element.getGridNeighbours()).intersection(elements)
            if let jump = jumps[element] {
                n.insert(jump)
            }
            return Array(n)
        }

        let search = BreadthFirstSearch(
            elements: coords,
            start: start,
            goal: end,
            getNeighbours: getNeighbours
        )
        let path = search.run().path
        return path.count - 1
    }


    private func getCoords(from data: String) -> (Coordinate, Coordinate, [Coordinate], [Coordinate: Coordinate]) {
        var coords: [Coordinate] = []
        var jumpParts: [JumpPart] = []
        for (rowNo, row) in data.components(separatedBy: .newlines).enumerated() {
            for (colNo, chr) in row.enumerated() {
                if chr == "." {
                    let coordinate = Coordinate(x: colNo, y: rowNo)
                    coords.append(coordinate)
                } else if chr.isUppercase {
                    let coordinate = Coordinate(x: colNo, y: rowNo)
                    let jumpPart = JumpPart(coordinate: coordinate, letter: String(chr))
                    jumpParts.append(jumpPart)
                }
            }
        }
        let (start, end, jumps) = pair(jumpParts: jumpParts, coords: coords)
        return (start, end, coords, jumps)
    }


    private func pair(jumpParts: [JumpPart], coords: [Coordinate]) -> (Coordinate, Coordinate, [Coordinate: Coordinate]) {
        var result: [Coordinate: Coordinate] = [:]
        var pairs: [[JumpPart]] = []
        var jumpParts = jumpParts
        while !jumpParts.isEmpty {
            let jp = jumpParts.removeFirst()
            let neighbourCoords = Set(jp.coordinate.getGridNeighbours())
            for (i, partner) in jumpParts.enumerated() {
                if neighbourCoords.contains(partner.coordinate) {
                    jumpParts.remove(at: i)
                    pairs.append([jp, partner])
                    break
                }
            }
        }
        var jumpPairs: [String: [Coordinate]] = [:]
        let coords = Set(coords)
        for pair in pairs {
            let n = Set(pair.map({ $0.coordinate }).flatMap({ $0.getGridNeighbours() }))
            let coord = coords.intersection(n).first!
            let name = pair.map({ $0.letter }).joined()
            jumpPairs[name, default: []].append(coord)
        }
        var start: Coordinate = Coordinate.origin
        var end: Coordinate = Coordinate.origin
        for (name, pair) in jumpPairs {
            if name == "AA" {
                start = pair[0]
            } else if name == "ZZ" {
                end = pair[0]
            } else {
                assert(pair.count == 2)
                result[pair[0]] = pair[1]
                result[pair[1]] = pair[0]
            }
        }
        return (start, end, result)
    }
}


private struct JumpPart: Hashable, CustomDebugStringConvertible {
    let coordinate: Coordinate
    let letter: String


    func hash(into hasher: inout Hasher) {
        hasher.combine(coordinate)
    }


    var debugDescription: String {
        return "\(letter)\(coordinate)"
    }
}


private let input1 = """
         A
         A
  #######.#########
  #######.........#
  #######.#######.#
  #######.#######.#
  #######.#######.#
  #####  B    ###.#
BC...##  C    ###.#
  ##.##       ###.#
  ##...DE  F  ###.#
  #####    G  ###.#
  #########.#####.#
DE..#######...###.#
  #.#########.###.#
FG..#########.....#
  ###########.#####
             Z
             Z
"""


private let input2 = """
                   A
                   A
  #################.#############
  #.#...#...................#.#.#
  #.#.#.###.###.###.#########.#.#
  #.#.#.......#...#.....#.#.#...#
  #.#########.###.#####.#.#.###.#
  #.............#.#.....#.......#
  ###.###########.###.#####.#.#.#
  #.....#        A   C    #.#.#.#
  #######        S   P    #####.#
  #.#...#                 #......VT
  #.#.#.#                 #.#####
  #...#.#               YN....#.#
  #.###.#                 #####.#
DI....#.#                 #.....#
  #####.#                 #.###.#
ZZ......#               QG....#..AS
  ###.###                 #######
JO..#.#.#                 #.....#
  #.#.#.#                 ###.#.#
  #...#..DI             BU....#..LF
  #####.#                 #.#####
YN......#               VT..#....QG
  #.###.#                 #.###.#
  #.#...#                 #.....#
  ###.###    J L     J    #.#.###
  #.....#    O F     P    #.#...#
  #.###.#####.#.#####.#####.###.#
  #...#.#.#...#.....#.....#.#...#
  #.#####.###.###.#.#.#########.#
  #...#.#.....#...#.#.#.#.....#.#
  #.###.#####.###.###.#.#.#######
  #.#.........#...#.............#
  #########.###.###.#############
           B   J   C
           U   P   P
"""
