//
//  Data22.swift
//  AdventOfCode2018
//
//  Created by gary on 28/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation

struct Data22 {
    struct Input {
        let depth: Int
        let target: Coordinate
    }


    static let test1 = Input(depth: 510, target: Coordinate(x: 10, y: 10))

    static let input = Input(depth: 9171, target: Coordinate(x: 7, y: 721))
}
