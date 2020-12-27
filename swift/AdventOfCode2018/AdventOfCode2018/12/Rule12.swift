//
//  Rule12.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

struct Rule12 {
    let pattern: String
    let result: String

    init(string: String) {
        let parts = string.components(separatedBy: " => ")
        self.pattern = parts[0]
        self.result = parts[1]
    }
}


struct Rules12 {
    let mapping: [String: String]

    init(string: String) {
        var mapping: [String: String] = [:]
        for line in string.split(separator: "\n") {
            let parts = line.components(separatedBy: " => ")
            mapping[parts[0]] = parts[1]
        }
        self.mapping = mapping
    }


    func map(input: String) -> String {
        return mapping[input] ?? "."
    }
}
