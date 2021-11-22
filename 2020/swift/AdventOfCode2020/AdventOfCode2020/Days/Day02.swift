//
//  Day02.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Foundation

private let pattern = #"^(\d+)-(\d+) (\w): (\w+)$"#

private let testInput = [
    ["1", "3", "a", "abcde"],
    ["1", "3", "b", "cdefg"],
    ["2", "9", "c", "ccccccccc"]
]

private struct Password {
    let lower: Int
    let upper: Int
    let chr: Character
    let password: String


    init(_ parts: [String]) {
        self.lower = Int(parts[0])!
        self.upper = Int(parts[1])!
        self.chr = Character(parts[2])
        self.password = parts[3]
    }


    var isValid1: Bool {
        let c = password.filter({ $0 == chr }).count
        return lower <= c && c <= upper
    }


    var isValid2: Bool {
        let lowerIndex = password.index(password.startIndex, offsetBy: lower - 1)
        let c1 = password[lowerIndex] == chr
        let upperIndex = password.index(password.startIndex, offsetBy: upper - 1)
        let c2 = password[upperIndex] == chr
        return c1 != c2
    }
}


func day02() -> (Int, Int) {
    tests()

    let passwords = String.lines(forDay: 2)
        .map({ $0.match(pattern: pattern) })
        .map(Password.init)

    let c1 = passwords.filter({ $0.isValid1 }).count
    let c2 = passwords.filter({ $0.isValid2 }).count

    return (c1, c2)
}


private func tests() {
    let p1 = Password(testInput[0]).isValid2
    assert(p1 == true)
    let p2 = Password(testInput[1]).isValid2
    assert(p2 == false)
    let p3 = Password(testInput[2]).isValid2
    assert(p3 == false)
}
