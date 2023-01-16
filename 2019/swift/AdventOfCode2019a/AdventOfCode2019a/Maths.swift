//
//  Maths.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation


func gcd(a: Int, b: Int) -> Int {
    if a < 0 {
        if b < 0 {
            return gcd(a: -a, b: -b)
        } else {
            return gcd(a: -a, b: b)
        }
    }
    if b < 0 {
        return gcd(a: a, b: -b)
    }
    if a < b {
        return gcd(a: b, b: a)
    }
    if b == 0 {
        return a < 0 ? -a : a
    }
    return gcd(a: b, b: a % b)
}


func lcm(a: Int, b: Int) -> Int {
    abs(a) * (abs(b) / gcd(a: a, b: b))
}


func hypot(p1: Point, p2: Point) -> Double {
    let a = Double(p2.x - p1.x)
    let b = Double(p2.y - p1.y)
    return (a*a + b*b).squareRoot()
}


func manhattan(p1: Point, p2: Point) -> Int {
    abs(p1.x - p2.x) + abs(p1.y - p2.y)
}


struct Point: Hashable, CustomDebugStringConvertible {
    let x: Int
    let y: Int

    static let origin = Point(x: 0, y: 0)


    static func * (lhs: Int, rhs: Point) -> Point {
        Point(x: lhs * rhs.x, y: lhs * rhs.y)
    }


    static func / (lhs: Point, rhs: Int) -> Point {
        Point(x: lhs.x / rhs, y: lhs.y / rhs)
    }


    static func + (lhs: Point, rhs: Point) -> Point {
        Point(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }


    static func - (lhs: Point, rhs: Point) -> Point {
        Point(x: lhs.x - rhs.x, y: lhs.y - rhs.y)
    }


    var debugDescription: String {
        "(\(x), \(y))"
    }
}
