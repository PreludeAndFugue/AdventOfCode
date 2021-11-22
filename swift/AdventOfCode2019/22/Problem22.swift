//
//  Problem22.swift
//  AdventOfCode2019
//
//  Created by gary on 27/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

private let regex1 = try! NSRegularExpression(
    pattern: "cut (-?\\d+)",
    options: []
)
private let regex2 = try! NSRegularExpression(
    pattern: "deal with increment (\\d+)",
    options: []
)
private let regex3 = try! NSRegularExpression(
    pattern: "deal into new stack",
    options: []
)

final class Problem22: Problem {
    enum Shuffle {
        case cut(Int)
        case dealIntoNewStack
        case dealWithIncrement(Int)


        init(string: String) {
            let range = NSRange(location: 0, length: string.utf16.count)
            if let match1 = regex1.firstMatch(in: string, options: [], range: range) {
                let n = getInt(from: match1.range(at: 1), forString: string)
                self = .cut(n)
            } else if let match2 = regex2.firstMatch(in: string, options: [], range: range) {
                let n = getInt(from: match2.range(at: 1), forString: string)
                self = .dealWithIncrement(n)
            } else if let _ = regex3.firstMatch(in: string, options: [], range: range) {
                self = .dealIntoNewStack
            } else {
                fatalError(string)
            }
        }
    }


    private let file = "22/data22.txt"
    private lazy var input = { try! String(contentsOfFile: path + file) }()

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 22, r1, r2)
    }
}


// MARK: - Public

extension Problem22 {
    func dealIntoNewStack(cards: [Int]) -> [Int] {
        return cards.reversed()
    }


    func cut(n: Int, cards: [Int]) -> [Int] {
        if n < 0 {
            let m = cards.count + n
            return Array(cards[m...] + cards[..<m])
        } else {
            assert(n < cards.count)
            return Array(cards[n...] + cards[..<n])
        }
    }


    func deal(n: Int, cards: [Int]) -> [Int] {
        var result = Array(repeating: 0, count: cards.count)
        let count = cards.count
        for (i, m) in cards.enumerated() {
            let j = (n * i) % count
            result[j] = m
        }
        return result
    }
}


extension Problem22 {
    func dealIntoNewStack(i: Int, count: Int) -> Int {
        count - i - 1
    }


    func cut(i: Int, n: Int, count: Int) -> Int {
        if n > 0 {
            return (i + count - n) % count
        } else {
            return (i + abs(n)) % count
        }
    }


    func deal(i: Int, n: Int, count: Int) -> Int {
        (n * i) % count
    }
}


// MARK: - Private

private extension Problem22 {
    private func part1() -> Int {
        let shuffles = parseInput(input)
        let count = 10_007
        var position = 2019
        for shuffle in shuffles {
            position = doShuffle(shuffle, toPosition: position, count: count)
        }
        return position
    }


    private func part2() -> Int {
        let shuffles = parseInput(input)
        let x = 119315717514047
        let y = 101741582076661
        var position = 0
        for shuffle in shuffles {
            position = doShuffle(shuffle, toPosition: position, count: x)
        }
        
        let z = modularPower(base: UInt(position), exponent: UInt(y), modulus: UInt(x))
        print(position)
        print(x)
        print(z)
        return 0
    }


    private func parseInput(_ input: String) -> [Shuffle] {
        input.trimmingCharacters(in: .newlines)
            .components(separatedBy: .newlines)
            .map({ Shuffle(string: $0) })
    }


    private func doShuffle(_ shuffle: Shuffle, toPosition position: Int, count: Int) -> Int {
        switch shuffle {
        case .cut(let n):
            return cut(i: position, n: n, count: count)
        case .dealIntoNewStack:
            return dealIntoNewStack(i: position, count: count)
        case .dealWithIncrement(let n):
            return deal(i: position, n: n, count: count)
        }
    }


    private func doShuffle(_ shuffle: Shuffle, to cards: [Int]) -> [Int] {
        switch shuffle {
        case .cut(let n):
            return cut(n: n, cards: cards)
        case .dealIntoNewStack:
            return dealIntoNewStack(cards: cards)
        case .dealWithIncrement(let n):
            return deal(n: n, cards: cards)
        }
    }
}


private func getInt(from nsrange: NSRange, forString string: String) -> Int {
    let startIndex = string.index(string.startIndex, offsetBy: nsrange.lowerBound)
    let endIndex = string.index(string.startIndex, offsetBy: nsrange.upperBound)
    let intString = string[startIndex..<endIndex]
    return Int(String(intString))!
}
