//
//  Array+Extensions.swift
//  AdventOfCode2019
//
//  Created by gary on 20/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

extension Array {
    func repeated(count: Int) -> Array<Element> {
        var result = self
        for _ in 0..<count - 1 {
            result += self
        }
        return result
    }


    var isNotEmpty: Bool {
        return !isEmpty
    }
}
