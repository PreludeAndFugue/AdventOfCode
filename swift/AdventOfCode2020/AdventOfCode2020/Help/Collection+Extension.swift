//
//  Collection+Extension.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Foundation

extension Collection where Element: AdditiveArithmetic {
    func sum() -> Element {
        reduce(.zero, +)
    }
}


extension Collection where Element: Numeric {
    func product() -> Element {
        reduce(1, *)
    }
}
