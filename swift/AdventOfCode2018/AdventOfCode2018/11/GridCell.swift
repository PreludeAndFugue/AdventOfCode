//
//  GridCell.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

struct GridCell {
    let x: Int
    let y: Int

    func power(serialNumber: Int) -> Int {
        let rackId = x + 10
        var powerLevel = y * rackId
        powerLevel += serialNumber
        powerLevel *= rackId
        let hundreds = (powerLevel % 1000)
        powerLevel = hundreds < 100 ? 0 : (hundreds - (hundreds % 100))/100
        return powerLevel - 5
    }
}
