//
//  Day10.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

func day10() {
//    let s = test5.trimmingCharacters(in: .whitespacesAndNewlines)
//        .split(separator: "\n")
//        .map({ String($0) })
    let s = get(file: "10")
        .split(separator: "\n")
        .map({ String($0) })

    let points = makePoints(map: s)

    let p1 = part1(points: points)
    print(p1)
}


private func part1(points: [Point]) -> Int {
    var map: [Point: [Point: (Point, Double)]] = [:]
    for (i, p1) in points.enumerated() {
        for p2 in points[(i + 1)...] {
            let d = hypot(p1: p1, p2: p2)
            var v = p2 - p1
            let g = gcd(a: v.x, b: v.y)
            v = v / g
            map[p1, default: [:]][p2] = (v, d)
            map[p2, default: [:]][p1] = (-1 * v, d)
        }
    }

    var bestCount = 0
//    var bestPoint = Point.origin
    for (_, values) in map {
        var s: Set<Point> = []
        for (point, _) in values.values {
            s.insert(point)
        }
        if s.count > bestCount {
            bestCount = s.count
//            bestPoint = p
        }
    }
    return bestCount
}


private func makePoints(map: [String]) -> [Point] {
    var points: [Point] = []
    for (j, row) in map.enumerated() {
        for (i, ch) in row.enumerated() {
            if ch == "#" {
                let p = Point(x: i, y: j)
                points.append(p)
            }
        }
    }
    return points
}


private let test1 = """
.#..#
.....
#####
....#
...##
"""

private let test2 = """
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

private let test3 = """
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

private let test4 = """
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

private let test5 = """
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
