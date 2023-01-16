//
//  Day10.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

private typealias Map = [Point: [Point: (Point, Double)]]
private typealias Part2 = [Point: (Point, Double)]


func day10() {
//    let s = test5.trimmingCharacters(in: .whitespacesAndNewlines)
//        .split(separator: "\n")
//        .map({ String($0) })
    let s = get(file: "10")
        .split(separator: "\n")
        .map({ String($0) })

    let points = makePoints(map: s)
    let map = makeMap(points: points)

    let (p1, bestPoint) = part1(map: map)
    print(p1)

    let data = map[bestPoint]!
    let p2 = part2(point: bestPoint, data: data)
    print(p2)
}


private func part1(map: Map) -> (Int, Point) {
    var bestCount = 0
    var bestPoint = Point.origin
    for (p, values) in map {
        var s: Set<Point> = []
        for (point, _) in values.values {
            s.insert(point)
        }
        if s.count > bestCount {
            bestCount = s.count
            bestPoint = p
        }
    }
    return (bestCount, bestPoint)
}


private func part2(point: Point, data: Part2) -> Int {
    var result: [Double: [(Double, Point)]] = [:]
    for (k, v) in data {
        let (vector, d) = v
        let a = getAngle(point: vector)
        result[a, default: []].append((d, k))
    }
    let angles = result.keys.sorted()
    var counter = 0
    var rotation = 1
    while true {
        for angle in angles {
            let items = result[angle]!
            if items.count >= rotation {
                counter += 1
            }
            if counter == 200 {
                let p = items[rotation - 1].1
                return 100 * p.x + p.y
            }
        }
        rotation += 1
    }
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


private func makeMap(points: [Point]) -> [Point: [Point: (Point, Double)]] {
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
    return map
}


private func getAngle(point: Point) -> Double {
    let a = atan2(Double(point.y), Double(point.x))
    var b = a < 0 ? 2 * Double.pi + a : a
    b += Double.pi / 2
    if b >= 2 * Double.pi {
        return b - 2 * Double.pi
    } else {
        return b
    }
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
