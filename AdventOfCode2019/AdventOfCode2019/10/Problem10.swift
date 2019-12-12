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
        let base = Coordinate(x: 11, y: 13)
//        let coords = makeInput(string: string5)
        let coords = input
        var groups = groupByAngle(coordinates: coords, source: base)
        let angles = groups.keys.sorted()
        var vapourisedList: [Coordinate] = []
        while isNotEmpty(groups) {
            for angle in angles {
                var coords = groups[angle, default: []]
                if coords.isEmpty { continue }
                let coord = coords.removeFirst()
                vapourisedList.append(coord.1)
                groups[angle] = coords
            }
        }
        let c = vapourisedList[199]
        return 100 * c.x + c.y
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
        let best = counts.sorted(by: { $0.value > $1.value }).first!
        print(best.key)
        return best.value
    }


    typealias CoordWithDistance = (Double, Coordinate)

    /// Group coords by angle and sort the group by distance from source.
    ///
    ///   - coords: The coordinates to group.
    ///   - source: The source to measure distance.
    private func groupByAngle(coordinates: [Coordinate], source: Coordinate) -> [Double: [CoordWithDistance]] {
        var groups: [Double: [CoordWithDistance]] = [:]
        for coord in coordinates {
            let vector = coord - source
            // Rotate angles so that smallest angle is pointing up
            var angle = vector.theta + Double.pi/2
            angle = angle < 0 ? angle + 2*Double.pi : angle
            groups[angle, default: []].append((vector.length, coord))
        }
        for (angle, coordsWithDistance) in groups {
            groups[angle] = coordsWithDistance.sorted(by: { $0.0 < $1.0 })
        }
        return groups
    }


    private func isNotEmpty(_ groups: [Double: [CoordWithDistance]]) -> Bool {
        for value in groups.values {
            if !value.isEmpty {
                return true
            }
        }
        return false
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
//                fatalError()
                continue
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

private let string6 = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
"""
