//
//  Day01.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Algorithms
import Foundation

func day01() -> (Int, Int) {
    let input = try! String.numbers(forDay: 1)
    let p1 = input.combinations(ofCount: 2)
        .first(where: { $0.sum() == 2020 })
        .map({ $0.product() })!
    let p2 = input.combinations(ofCount: 3)
        .first(where: { $0.sum() == 2020 })
        .map({ $0.product() })!
    return (p1, p2)
}
