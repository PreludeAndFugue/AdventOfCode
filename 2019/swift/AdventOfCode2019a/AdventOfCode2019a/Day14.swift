//
//  Day14.swift
//  AdventOfCode2019a
//
//  Created by gary on 16/01/2023.
//

import Foundation

func day14() {
//    let s = test5.trimmingCharacters(in: .whitespacesAndNewlines)
    let s = get(file: "14")
    let eqns = parse(s: s)

    let p1 = part1(eqns: eqns)
    print(p1)
}


private func part1(eqns: [Equation]) -> Int {
    var fuelEqn = eqns.filter({ $0.isFuel }).first!
    let oreEqns = eqns.filter({ $0.containsOre })
    let otherEqns = eqns.filter({ !$0.isFuel && !$0.containsOre })

    let c = 1 + oreEqns.count + otherEqns.count
    assert(c == eqns.count)

    for _ in 0...2 {
        while true {
            var didChange = false
            for eqn in otherEqns {
                if fuelEqn.contains(name: eqn.rhs.name) {
                    let change = fuelEqn.substitute(eqn: eqn)
                    if change {
    //                    print(fuelEqn)
                        didChange = true
                    }
                }
            }
            if !didChange {
                break
            }
        }
        while true {
            var didChange = false
            for eqn in oreEqns {
                if fuelEqn.contains(name: eqn.rhs.name) {
                    let change = fuelEqn.substitute(eqn: eqn)
                    if change {
    //                    print(fuelEqn)
                        didChange = true
                    }
                }
            }
            if !didChange {
                break
            }
        }
    }
    return fuelEqn.lhs.filter({ $0.name == "ORE" }).first!.quantity
}


private func parse(s: String) -> [Equation] {
    var eqns: [Equation] = []
    for line in s.split(separator: "\n") {
        let parts = line.split(separator: " => ")
        let lhs = parts[0]
        let rhs = parts[1]
        let rhsParts = rhs.split(separator: " ")
        var lhsSymbols: [Symbol] = []
        for x in lhs.split(separator: ", ") {
            let x1 = x.split(separator: " ")
            let s = Symbol(quantity: Int(x1[0])!, name: String(x1[1]))
            lhsSymbols.append(s)
        }
        let e = Equation(
            lhs: lhsSymbols,
            rhs: Symbol(quantity: Int(rhsParts[0])!, name: String(rhsParts[1]))
        )
        eqns.append(e)
    }
    return eqns
}


private struct Symbol: CustomDebugStringConvertible {
    var quantity: Int
    let name: String

    var debugDescription: String {
        "\(quantity)\(name)"
    }
}


private struct Equation: CustomDebugStringConvertible {
    var lhs: [Symbol]
    var rhs: Symbol


    var isFuel: Bool {
        rhs.name == "FUEL"
    }


    var containsOre: Bool {
        for s in lhs {
            if s.name == "ORE" {
                return true
            }
        }
        return false
    }


    func contains(name: String) -> Bool {
        for s in lhs {
            if s.name == name {
                return true
            }
        }
        return false
    }


    mutating func substitute(eqn: Equation) -> Bool {
        let s = eqn.rhs
        guard let s1 = lhs.filter({ $0.name == s.name }).first else {
            return false
        }
        if s1.quantity < 0 {
            return false
        }
        if s1.quantity == s.quantity {
            lhs = lhs.filter({ $0.name != s1.name }) + eqn.lhs
        } else if s1.quantity > s.quantity {
            let n = Symbol(quantity: s1.quantity - s.quantity, name: s1.name)
            lhs = lhs.filter({ $0.name != s1.name }) + eqn.lhs + [n]
        } else {
//            print("not enough")
            let n = Symbol(quantity: s1.quantity - s.quantity, name: s1.name)
            lhs = lhs.filter({ $0.name != s1.name }) + eqn.lhs + [n]
        }
        combine()
        return true
    }


    private mutating func combine() {
        var combined: [String: Int] = [:]
        for s in lhs {
            combined[s.name, default: 0] += s.quantity
        }
        lhs = combined.map({ Symbol(quantity: $0.value, name: $0.key) })
    }


    var debugDescription: String {
        "Eqn(lhs: \(lhs), rhs: \(rhs))"
    }
}


private let test1 = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""

private let test2 = """
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""

private let test3 = """
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
"""

private let test4 = """
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
"""

private let test5 = """
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
"""
