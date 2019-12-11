//
//  Problem10.swift
//  AdventOfCode2019
//
//  Created by gary on 11/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem10: Problem {
    private let file = "10/data10.txt"
    private lazy var input: [Coordinate] = {
        let string = try! String(contentsOfFile: self.path + self.file)
        return makeInput(string: string)
    }()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 10, r1, r2)
    }
}


// MARK: - Private

private extension Problem10 {
    private func part1() -> Int {
//        let coords = makeInput(string: string5)
        let coords = input
        var coordCount: [Coordinate: Int] = [:]
        for coord in coords {
            let angles = getUniqueAngles(for: coord, otherCoordinates: coords)
            coordCount[coord] = angles.count
        }
        return getMaxCoordinateCount(counts: coordCount)
    }


    private func part2() -> Int {
        return 0
    }


    private func getUniqueAngles(for coordinate: Coordinate, otherCoordinates: [Coordinate]) -> Set<Double> {
        var angles: Set<Double> = []
        for other in otherCoordinates {
            if other == coordinate { continue }
            let vector = other - coordinate
            angles.insert(vector.theta)
        }
        return angles
    }


    private func getMaxCoordinateCount(counts: [Coordinate: Int]) -> Int {
        return counts.sorted(by: { $0.value > $1.value }).first!.value
    }
}



private func makeInput(string: String) -> [Coordinate] {
    var coordinates: [Coordinate] = []
    for (rowNo, row) in string.trimmingCharacters(in: .newlines).split(separator: "\n").enumerated() {
        for (colNo, chr) in row.enumerated() {
            switch chr {
            case ".":
                continue
            case "#":
                let coordinate = Coordinate(x: colNo, y: rowNo)
                coordinates.append(coordinate)
            default:
                fatalError()
            }
        }
    }
    return coordinates
}


private let string1 = """
.#..#
.....
#####
....#
...##
"""

private let string2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""

private let string3 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""

private let string4 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""

private let string5 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
