//
//  Maths.swift
//  AdventOfCode2019
//
//  Created by gary on 13/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

func gcd(a: Int, b: Int) -> Int {
    var a = a
    var b = b
    while b != 0 {
        (a, b) = (b, a % b)
    }
    return abs(a)
}


func gcd(numbers: [Int]) -> Int {
    numbers.reduce(0, { gcd(a: $0, b: $1) })
}


func lcm(a: Int, b: Int) -> Int {
    (a / gcd(a: a, b: b)) * b
}


func lcm(numbers: [Int]) -> Int {
    numbers.reduce(1, { lcm(a: $0, b: $1) })
}
