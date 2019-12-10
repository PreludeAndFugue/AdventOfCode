//
//  Problem08.swift
//  AdventOfCode2019
//
//  Created by gary on 08/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem08: Problem {
    private let file = "8/data08.txt"
    private lazy var input = self.makeInput()

    private let totalSize = 15_000
    private let width = 25
    private let height = 6

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 8, r1, r2)
    }
}


// MARK: - Private

private extension Problem08 {
    private func makeInput() -> [[[Int]]] {
        let string = try! String(contentsOfFile: path + file).trimmingCharacters(in: .newlines)
        var layers: [[[Int]]] = []
        let size = string.count
        var rows: [[Int]] = []
        for i in 0..<(size / width) {
            let a = string.index(string.startIndex, offsetBy: i * width)
            let b = string.index(string.startIndex, offsetBy: (i + 1) * width)
            let row = string[a..<b].map({ $0.wholeNumberValue! })
            rows.append(row)
            if (i + 1) % height == 0 {
                layers.append(rows)
                rows = []
            }
        }
        return layers
    }


    private func part1() -> Int {
        assert(input.flatMap({ $0 }).flatMap({ $0 }).count == totalSize)
        let layer = input
            .map(countLayerValues(layer:))
            .sorted(by: { $0[0, default: 0] < $1[0, default: 0] })
            .first!
        let result = layer[1, default: 0] * layer[2, default: 0]
        return result
    }


    private func part2() -> Int {
        var result = Array(repeating: Array(repeating: 0, count: 25), count: 6)
        for layer in input.reversed() {
            for (rowIndex, row) in layer.enumerated() {
                for (colIndex, value) in row.enumerated() {
                    if value == 2 {
                        continue
                    }
                    result[rowIndex][colIndex] = value
                }
            }
        }
        let output = result
            .map({ $0
                .map({ $0 == 0 ? " " : String($0) })
                .joined()
            })
            .joined(separator: "\n")
        print(output)
        return 1
    }


    private func countLayerValues(layer: [[Int]]) -> [Int: Int] {
        var result: [Int: Int] = [:]
        for value in layer.flatMap({ $0 }) {
            result[value, default: 0] += 1
        }
        return result
    }
}
