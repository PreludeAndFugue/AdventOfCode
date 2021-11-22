//
//  AscendingNumbers.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

/// Generate integers where the digits ascend from left to right.
///
/// For example:
///    1, 2, 3, 11, 12, 13, 22, 23, 111, 156, 477, 589, 999, 1111,
///    1234
final class AscendingNumbers {
    private var n: Int

    init(start: Int) {
        self.n = makeFirst(start)
    }


    var next: Int {
        let current = n
        n = increment(n)
        return current
    }
}


// MARK: - Private

private extension AscendingNumbers {
    func increment(_ n: Int) -> Int {
        return makeFirst(n + 1)
    }
}


private func makeFirst(_ n: Int) -> Int {
    var digits = n.base10Digits
    let indices = digits.indices
    for (i, j) in zip(indices.dropLast(), indices.dropFirst()) {
        if digits[j] < digits[i] {
            digits[j] = digits[i]
        }
    }
    return Int(fromDigits: digits)
}

