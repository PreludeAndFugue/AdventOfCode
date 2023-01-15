//
//  Day03.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

func day03() {
    let f = get(file: "03").trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
    let path1 = String(f[0])
    let path2 = String(f[1])
    let points1 = makePoints(from: path1)
    let points2 = makePoints(from: path2)
    let intersection = Set(points1).intersection(points2)

    let p1 = part1(intersection: intersection)
    print(p1)

    let p2 = part2(points1: points1, points2: points2, intersection: intersection)
    print(p2)
}


private func part1(intersection: Set<Point>) -> Int {
    intersection.map({ manhattan(p1: $0, p2: .origin) }).min()!
}


private func part2(points1: [Point], points2: [Point], intersection: Set<Point>) -> Int {
    intersection.map({ points1.firstIndex(of: $0)! + points2.firstIndex(of: $0)! + 2 }).min()!
}


private func makePoints(from path: String) -> [Point] {
    var points: [Point] = []
    var x = 0
    var y = 0
    for a in path.split(separator: ",") {
        let direction = a.first!
        let count = Int(a[a.index(after: a.startIndex)...])!
        switch direction {
        case "L":
            for _ in 0..<count {
                x -= 1
                points.append(Point(x: x, y: y))
            }
        case "R":
            for _ in 0..<count {
                x += 1
                points.append(Point(x: x, y: y))
            }
        case "U":
            for _ in 0..<count {
                y += 1
                points.append(Point(x: x, y: y))
            }
        case "D":
            for _ in 0..<count {
                y -= 1
                points.append(Point(x: x, y: y))
            }
        default:
            fatalError()
        }
    }
    return points
}
