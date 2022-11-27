//
//  main.swift
//  AdventOfCode2022
//
//  Created by gary on 26/11/2022.
//

import Foundation

let d = Day01()

do {
    let (p1, p2) = try d.run()
    print("Part 1:", p1)
    print("Part 2:", p2)
} catch let error {
    print(error)
}
