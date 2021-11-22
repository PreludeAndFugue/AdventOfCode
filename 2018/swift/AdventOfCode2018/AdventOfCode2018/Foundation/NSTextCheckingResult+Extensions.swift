//
//  NSTextCheckingResult+Extensions.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

extension NSTextCheckingResult {
    func groups(for string: String) -> [String] {
        var parts: [String] = []
        for i in 1..<numberOfRanges {
            guard let r = Range(range(at: i), in: string) else {
                parts.append("")
                continue
            }
            let part = String(string[r])
            parts.append(part)
        }
        return parts
    }
}
