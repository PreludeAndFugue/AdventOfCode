import Foundation

private let test = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


typealias Input = (patterns: [String], values: [String])


public func day08() {
    let testInput = parse(test)
    let input = parse(read("day08"))

    let t2 = part2(input: testInput)
    assert(t2 == 61229)

    let p2 = part2(input: input)
    print(p2)
}


private func parse(_ string: String) -> [Input] {
    var result: [Input] = []
    for a in string.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n") {
        let b = a.components(separatedBy: " | ")
        let patterns = b.first!.split(separator: " ").map({ String($0) })
        let values = b.last!.split(separator: " ").map({ String($0) })
        let input = (patterns: patterns, values: values)
        result.append(input)
    }
    return result
}


private func sort(_ string: String) -> String {
    string.sorted().map({ String($0) }).joined()
}


func solve(patterns: [String], values: [String]) -> Int {
    let sortedPatterns = patterns.map({ sort($0) })
    let groups = Dictionary(grouping: sortedPatterns, by: { $0.count })
    let one = groups[2]!.first!
    let seven = groups[3]!.first!
    let four = groups[4]!.first!
    let subFour = Set(four).subtracting(one)
    let fiveParts = groups[5]!
    let sixParts = groups[6]!
    let eight = groups[7]!.first!

    let two = fiveParts.first(where: { !Set($0).isSuperset(of: one) && !Set($0).isSuperset(of: subFour) })!
    let three = fiveParts.first(where: { Set($0).isSuperset(of: one) })!
    let five = fiveParts.first(where: { Set($0).isSuperset(of: subFour) })!

    let nine = sixParts.first(where: { Set($0).isSuperset(of: four) && Set($0).isSuperset(of: one) })!
    let six = sixParts.first(where: { Set($0).isSuperset(of: subFour) && !Set($0).isSuperset(of: seven) })!
    let zero = sixParts.first(where: { Set($0).isSuperset(of: seven) && !Set($0).isSuperset(of: subFour) })!

    let mapping: [String: Int] = [
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9,
        zero: 0,
    ]
    let digits = values.map({ sort($0) })
        .map({ mapping[$0]! })
        .reversed()
        .enumerated()
        .map({ $0.element * Array(repeating: 10, count: $0.offset).reduce(1, *) })
    let n = digits.reduce(0, +)
    return n
}


func part2(input: [Input]) -> Int {
    var total = 0
    for x in input {
        let n = solve(patterns: x.patterns, values: x.values)
        total += n
    }
    return total
}
