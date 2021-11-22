//
//  Problem14.swift
//  AdventOfCode2019
//
//  Created by gary on 14/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

private struct Material: Hashable, CustomDebugStringConvertible {
    let name: String
    let quantity: Int

    var debugDescription: String {
        return "\(quantity) \(name)"
    }
}


private let ore = "ORE"
private let fuel = "FUEL"

private struct Relationship: CustomDebugStringConvertible {
    let lhs: [Material]
    let rhs: Material

    var containsOre: Bool {
        lhs.map({ $0.name }).contains(ore)
    }

    var containsFuel: Bool {
        rhs.name == fuel
    }

    var debugDescription: String {
        let left = lhs.map({ $0.debugDescription }).joined(separator: ", ")
        return "\(left) => \(rhs)"
    }
}


private class Matrix {
    let matrix: [[Int]]
    let allNames: [String]
    let nonOreNames: [String]
    let oreNames: [String]
    var fuelRow: [Int]

    init(relationships: [Relationship]) {
        var oreNames: Set<String> = []
        var nonOreNames: Set<String> = []
        for relationship in relationships {
            if relationship.containsOre {
                oreNames.insert(relationship.rhs.name)
                relationship.lhs.forEach({ oreNames.insert($0.name) })
            } else {
                nonOreNames.insert(relationship.rhs.name)
                relationship.lhs.forEach({ nonOreNames.insert($0.name) })
            }
        }
        oreNames.remove(ore)
        oreNames.remove(fuel)
        nonOreNames.remove(ore)
        nonOreNames.remove(fuel)
        nonOreNames.subtract(oreNames)

        self.oreNames = oreNames.sorted()
        self.nonOreNames = nonOreNames.sorted()
        self.allNames = [fuel] + self.oreNames + self.nonOreNames + [ore]

        var rows: [[Int]] = []
        var fuelRow: [Int]?
        for relationship in relationships {
            var row = Array(repeating: 0, count: allNames.count)
            let i = allNames.firstIndex(of: relationship.rhs.name)!
            row[i] = relationship.rhs.quantity
            for material in relationship.lhs {
                let j = allNames.firstIndex(of: material.name)!
                row[j] = -material.quantity
            }
            if relationship.containsFuel {
                fuelRow = row
            } else {
                rows.append(row)
            }
        }

        self.matrix = rows
        self.fuelRow = fuelRow!


//        print(allNames)
//        print("ore", self.oreNames)
//        print("no ore", self.nonOreNames)
    }


    func solve() -> Int {
        while anyLessThanZero(fuelElements()) {
            for (i, n) in fuelElements().enumerated() {
                if n < 0 {
                    let row = findRowWith(postiveIndex: i + 1)
                    updateSolution(withRow: row)
                }
            }
        }
        return -fuelRow.last!
    }


    func solve2() -> Int {
//        print("\n\n\n")
        let totalOre = 1_000_000_000_000
//        let totalOre = 1_000
        let orePerFuel = 579797


        var solution = Array(repeating: 0, count: fuelRow.count)
        solution[solution.endIndex - 1] = totalOre

//        print(matrix.map({ $0.map({ String($0) }).joined(separator: ", ") }).joined(separator: "\n"))
//        print(fuelRow)
//        print(solution)

        func hasOre() -> Bool { solution.last! > 0 }
        func addFuel(mult: Int = 1) { solution = zip(solution, fuelRow).map({ $0 + mult * $1 }) }
        func solutionElements() -> ArraySlice<Int> { solution[1...(solution.count - 2)] }
        func add(row: [Int], mult: Int = 1) { solution = zip(solution, row).map({ $0 + mult * $1 }) }
        func balanceSolution() {
            while anyLessThanZero(solutionElements()) {
                for (i, n) in solutionElements().enumerated() {
                    if n < 0 {
                        let row = findRowWith(postiveIndex: i + 1)
                        var mult = abs(solution[i + 1]) / row[i + 1]
                        if mult == 0 { mult = 1}

//                        print(i + 1)
//                        print(mult)
//                        print(row)
//                        print(solution)
                        add(row: row, mult: mult)
//                        print(solution)
//                        print("\n")
                    }
                }
            }
        }

        let baseFuel = totalOre / orePerFuel
//        print("base fuel", baseFuel)
        addFuel(mult: baseFuel)
//        solution[solution.endIndex - 1] = totalOre - orePerFuel * baseFuel
        balanceSolution()

        while hasOre() {
            let baseFuel = solution.last! / orePerFuel
            if baseFuel == 0 { break }
//            print("base fuel", baseFuel)
            addFuel(mult: baseFuel)
//            print("\n\n")
            balanceSolution()
//            print("add fuel")
//            print(solution)
//            print("\n\n")
        }

//        print(solution)
        return solution[0]
    }


    private func fuelElements() -> ArraySlice<Int> {
        fuelRow[1...(self.fuelRow.count - 2)]
    }


    private func anyLessThanZero(_ numbers: ArraySlice<Int>) -> Bool {
        for n in numbers {
            if n < 0 {
                return true
            }
        }
        return false
    }


    private func findRowWith(postiveIndex index: Int) -> [Int] {
        for row in matrix {
            if row[index] > 0 {
                return row
            }
        }
        fatalError()
    }


    private func updateSolution(withRow row: [Int]) {
        fuelRow = zip(fuelRow, row).map({ $0 + $1 })
    }
}


final class Problem14: Problem {
    private let file = "14/data14.txt"
    private lazy var input = try! String(contentsOfFile: path + file)

    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 14, r1, r2)
    }
}


// MARK: - Private

private extension Problem14 {
    private func part1() -> Int {
        let relationships = makeInput(string: input)
        let matrix = Matrix(relationships: relationships)
        return matrix.solve()
    }


    private func part2() -> Int {
        let relationships = makeInput(string: input)
        let matrix = Matrix(relationships: relationships)
        return matrix.solve2()
    }


    private func makeInput(string: String) -> [Relationship] {
        let data = string
            .trimmingCharacters(in: .newlines)
            .split(separator: "\n")
            .map({ $0.components(separatedBy: " => ") })
            .map({
                Relationship(
                    lhs: $0[0].components(separatedBy: ", ").map(parseElement(_:)),
                    rhs: parseElement($0[1])
                )
            })
        return data
    }


    private func parseElement(_ string: String) -> Material {
        let parts = string.components(separatedBy: " ")
        return Material(name: parts[1], quantity: Int(parts[0])!)
    }
}


private let input1 = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""


private let input2 = """
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""


private let input3 = """
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


private let input4 = """
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


private let input5 = """
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
