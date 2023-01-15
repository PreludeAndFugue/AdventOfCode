//
//  Help.swift
//  AdventOfCode2019a
//
//  Created by gary on 14/01/2023.
//

import Foundation

private let base = "/Users/gary/Documents/computing/_AdventOfCode/2019/day"


func get(file: String) -> String {
    let data = FileManager.default.contents(atPath: base + file + ".txt")!
    return String(data: data, encoding: .utf8)!
}


func getInts(file: String) -> [Int] {
    get(file: file).trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
        .map({ Int($0)! })
}


func getIncode(file: String) -> IntCode {
    get(file: file).trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: ",")
        .map({ Int($0)! })
}
