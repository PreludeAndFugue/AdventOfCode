//
//  Sequence+Extensions.swift
//  AdventOfCode2019
//
//  Created by gary on 01/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

import Foundation

extension Sequence where Element: Numeric {
    func sum() -> Element {
        reduce(0, +)
    }
}


// MARK: - Permutations

extension Sequence {
    func permutations(r: Int? = nil) -> [[Element]] {
        var result: [[Element]] = []
        let pool = Array(self)
        let n = pool.count
        let r_ = r ?? n
        if r_ > n {
            return result
        }
        var indices = Array(0..<n)
        var cycles = Array(stride(from: n, to: n - r_, by: -1))
        result.append(makeItem(pool: pool, indices: indices, r: r_))

        var didMakeItem = true
        while true {
            if didMakeItem {
                didMakeItem = false
            } else {
                // exit while loop
                break
            }
            for i in (0..<r_).reversed() {
                cycles[i] -= 1
                if cycles[i] == 0 {
                    indices = switchIndices(indices, i: i)
                    cycles[i] = n - i
                } else {
                    let j = cycles[i]
                    switchElements(&indices, i: i, j: j)
                    result.append(makeItem(pool: pool, indices: indices, r: r_))
                    didMakeItem = true
                    break
                }
            }
        }
        return result
    }


    private func makeItem(pool: [Element], indices: [Int], r: Int) -> [Element] {
        var result: [Element] = []
        for i in 0..<r {
            let index = indices[i]
            result.append(pool[index])
        }
        return result
    }


    private func switchIndices(_ indices: [Int], i: Int) -> [Int] {
        let n = indices.count
        var temp: [Int] = []
        for j in 0..<i {
            temp.append(indices[j])
        }
        for j in (i + 1)..<n {
            temp.append(indices[j])
        }
        temp.append(indices[i])
        return temp
    }


    private func switchElements(_ indices: inout [Int], i: Int, j: Int) {
        let minusJ = indices.endIndex.advanced(by: -j)
        let temp = indices[i]
        indices[i] = indices[minusJ]
        indices[minusJ] = temp
    }
}
