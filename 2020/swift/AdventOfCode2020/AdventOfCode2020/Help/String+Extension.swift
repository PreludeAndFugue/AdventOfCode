//
//  String+Extension.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Foundation
import System

private let base = "/Users/gary/Documents/computing/python/AdventOfCode/2020/swift/AdventOfCode2020/AdventOfCode2020/Input/"


// MARK: - Parsing input

extension String {
    static func input(forDay: Int) -> String {
        let dayString = String(format: "%02d", forDay)
        let file = "day\(dayString)"
        let path = Bundle.main.path(forResource: file, ofType: ".txt")!
        return try! String(contentsOfFile: path, encoding: .utf8)
    }


    static func lines(forDay: Int) -> [String] {
        input(forDay: forDay)
            .split(separator: "\n")
            .map(String.init)
            .map({ $0.trimmingCharacters(in: .whitespacesAndNewlines )})
    }


    static func numbers(forDay: Int) -> [Int] {
        input(forDay: forDay)
            .trimmingCharacters(in: .whitespacesAndNewlines)
            .split(separator: "\n")
            .map(String.init)
            .map({ Int($0)! })
    }
}


// MARK: - Regular expressions

extension String {
    func match(pattern: String) -> [String] {
        let re = try! NSRegularExpression(pattern: pattern, options: [])
        let range = NSRange(location: 0, length: count)
        guard let match = re.firstMatch(in: self, options: [], range: range) else {
            return []
        }
        var parts: [String] = []
        for i in 1..<match.numberOfRanges {
            let r = match.range(at: i)
            parts.append(self.range(r))
        }
        return parts
    }


    func range(_ nsRange: NSRange) -> String {
        let i1 = index(startIndex, offsetBy: nsRange.lowerBound)
        let i2 = index(startIndex, offsetBy: nsRange.upperBound)
        return String(self[i1..<i2])
    }
}
