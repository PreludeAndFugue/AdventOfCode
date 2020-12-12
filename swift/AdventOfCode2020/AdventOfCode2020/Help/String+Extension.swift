//
//  String+Extension.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Foundation
import System

private let base = "/Users/gary/Documents/computing/python/AdventOfCode/2020/swift/AdventOfCode2020/AdventOfCode2020/Input/"

extension String {
    static func input(forDay: Int) throws -> String {
        let dayString = String(format: "%02d", forDay)
        let file = "day\(dayString).txt"
        let path = base + file
        return try String(contentsOfFile: path, encoding: .utf8)
    }


    static func numbers(forDay: Int) throws -> [Int] {
        try input(forDay: forDay)
            .trimmingCharacters(in: .whitespacesAndNewlines)
            .split(separator: "\n")
            .map(String.init)
            .map({ Int($0)! })
    }
}
