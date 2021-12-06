import Foundation

private let test = """
3,4,3,1,2
"""


public func day06() {
    let testInput = parse(test)

    let url = Bundle.main.url(forResource: "day06", withExtension: "txt")!
    let string = try! String(contentsOf: url)
    let input = parse(string)

    tests(fish: testInput)

    let p1 = part(n: 80, input)
    print(p1)
    let p2 = part(n: 256, input)
    print(p2)
}


private func parse(_ string: String) -> [Int: Int] {
    let ns = string.trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: ",")
        .map({ Int($0)! })
    var fish: [Int: Int] = [
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0
    ]
    for n in ns {
        fish[n, default: 0] += 1
    }
    return fish
}


private func cycle(_ fish: [Int: Int]) -> [Int: Int] {
    [
        0: fish[1]!,
        1: fish[2]!,
        2: fish[3]!,
        3: fish[4]!,
        4: fish[5]!,
        5: fish[6]!,
        6: fish[7]! + fish[0]!,
        7: fish[8]!,
        8: fish[0]!
    ]
}


private func cycle(n: Int, _ fish: [Int: Int]) -> [Int: Int] {
    var f = fish
    for _ in 0..<n {
        f = cycle(f)
    }
    return f
}


private func part(n: Int, _ fish: [Int: Int]) -> Int {
    let f = cycle(n: n, fish)
    return f.values.reduce(0, +)
}


private func tests(fish: [Int: Int]) {
    assert(part(n: 80, fish) == 5934)
    assert(part(n: 256, fish) == 26984457539)
}
