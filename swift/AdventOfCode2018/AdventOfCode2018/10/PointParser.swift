//
//  PointParser.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let pattern = "position=<([ -]*)(\\d+), ([ -])*(\\d+)> velocity=<([ -])*(\\d+), ([ -])*(\\d+)>"

struct PointParser {
    let re = try! NSRegularExpression(pattern: pattern, options: [])

    func parse(string: String) -> Point {
        let range = NSRange(location: 0, length: string.utf16.count)
        guard let match = re.firstMatch(in: string, options: [], range: range) else {
            fatalError()
        }
        let groups = match.groups(for: string)
        let x = makeNumber(signString: groups[0], numberString: groups[1])
        let y = makeNumber(signString: groups[2], numberString: groups[3])
        let u = makeNumber(signString: groups[4], numberString: groups[5])
        let v = makeNumber(signString: groups[6], numberString: groups[7])
        return Point(x: x, y: y, u: u, v: v)
    }


    func parseAll(string: String) -> [Point] {
        var points: [Point] = []
        for line in string.split(separator: "\n") {
            points.append(parse(string: String(line)))
        }
        return points
    }


    func makeNumber(signString: String, numberString: String) -> Int {
        let number = Int(numberString) ?? 0
        if signString == "-" {
            return -number
        } else {
            return number
        }
    }
}
