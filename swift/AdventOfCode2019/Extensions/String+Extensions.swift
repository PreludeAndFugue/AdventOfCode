//
//  String+Extensions.swift
//  AdventOfCode2019
//
//  Created by gary on 08/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

extension String {
    func makeIntegers(separator: String) -> [Int] {
        return self
            .trimmingCharacters(in: .newlines)
            .components(separatedBy: separator)
            .compactMap(Int.init)
    }
}
