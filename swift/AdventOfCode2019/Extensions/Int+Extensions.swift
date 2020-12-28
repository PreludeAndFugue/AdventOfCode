//
//  Int+Extensions.swift
//  AdventOfCode2019
//
//  Created by gary on 04/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

extension Int {
    var base10Digits: [Int] {
        var digits: [Int] = []
        var n = self
        while true {
            let (q, r) = n.quotientAndRemainder(dividingBy: 10)
            digits.append(r)
            if q == 0 { break }
            n = q
        }
        return digits.reversed()
    }


    init(fromDigits digits: [Int]) {
        var result = 0
        for digit in digits.dropLast() {
            result += digit
            result *= 10
        }
        result += digits.last!
        self = result
    }
}


func modularPower(base: UInt, exponent: UInt, modulus: UInt) -> UInt {
    if modulus == 1 {
        return 0
    }
    let _ = (modulus - 1) * (modulus - 1)
    var result: UInt = 1
    var base = base % modulus
    var exponent = exponent
    while exponent > 0 {
        if (exponent % 2 == 1) {
            result = (result * base) % modulus
        }
        exponent = exponent >> 1
        base = (base * base) % modulus
    }
    return result
}
