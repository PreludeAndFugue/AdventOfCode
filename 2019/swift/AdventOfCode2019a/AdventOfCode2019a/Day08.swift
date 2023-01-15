//
//  Day08.swift
//  AdventOfCode2019a
//
//  Created by gary on 15/01/2023.
//

import Foundation

func day08() {
    let values = get(file: "08").trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "")
        .map({ Int($0)! })

    let width = 25
    let height = 6
    let length = width * height
    let layerCount = values.count / length

    var layers: [[Int]] = []
    var layer: [Int] = []
    for (i, value) in values.enumerated() {
        if i % length == 0 && !layer.isEmpty {
            layers.append(layer)
            layer = [value]
        } else {
            layer.append(value)
        }
    }
    layers.append(layer)

    assert(layers.count == layerCount)
    for layer in layers {
        assert(layer.count == length)
    }

    let p1 = part1(layers: layers)
    print(p1)

    part2(layers: layers)
}


private func part1(layers: [[Int]]) -> Int {
    var minLayer: [Int] = []
    var minCount = Int.max
    for layer in layers {
        let count = layer.filter({ $0 == 0 }).count
        if count < minCount {
            minCount = count
            minLayer = layer
        }
    }
    let ones = minLayer.filter({ $0 == 1 }).count
    let twos = minLayer.filter({ $0 == 2 }).count
    return ones * twos
}


private func part2(layers: [[Int]]) {
    let l = layers[0].count
    var result = Array(repeating: 0, count: l)
    for i in 0..<l {
        for layer in layers {
            let n = layer[i]
            if n != 2 {
                result[i] = n
                break
            }
        }
    }
    print(layer: result)
}


private func print(layer: [Int]) {
    for (i, n) in layer.enumerated() {
        if i % 25 == 0 {
            print()
        }
        print(n == 1 ? "#" : " ", terminator: "")
    }
    print()
}
