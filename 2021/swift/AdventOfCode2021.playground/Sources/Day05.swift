import Foundation

private let test = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


public func day05() {
    let testInput = parse(test)
    let input = parse(read("day05"))

    let t1 = testInput.flatMap({ range($0, diagonals: false) })
    assert(count(t1) == 5)

    let a1 = input.flatMap({ range($0, diagonals: false) })
    let p1 = count(a1)
    print(p1)

    let t2 = testInput.flatMap({ range($0, diagonals: true) })
    assert(count(t2) == 12)

    let a2 = input.flatMap({ range($0, diagonals: true) })
    let p2 = count(a2)
    print(p2)
}


private func parse(_ string: String) -> [[[Int]]] {
    return string.trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
        .map({ $0.components(separatedBy: " -> ") })
        .map({ $0.map({ $0.split(separator: ",") }) })
        .map({ $0.map({ $0.compactMap({ Int($0)! }) }) })
}


private func range(_ pair: [[Int]], diagonals: Bool) -> [Point] {
    let f = pair.first!
    let l = pair.last!
    let dx = l[0] - f[0]
    let dy = l[1] - f[1]
    if dx == 0 {
        let s = stride(from: f[1], through: l[1], by: dy < 0 ? -1 : 1)
        return s.map({ Point(x: f[0], y: $0) })
    }
    if dy == 0 {
        let s = stride(from: f[0], through: l[0], by: dx < 0 ? -1 : 1)
        return s.map({ Point(x: $0, y: f[1]) })
    }
    guard diagonals else { return [] }
    assert(abs(dx) == abs(dy))
    let sx = stride(from: f[0], through: l[0], by: dx < 0 ? -1 : 1)
    let sy = stride(from: f[1], through: l[1], by: dy < 0 ? -1 : 1)
    return zip(sx, sy).map({ Point(x: $0.0, y: $0.1) })
}


private func count(_ points: [Point]) -> Int {
    var counter: [Point: Int] = [:]
    for point in points {
        counter[point, default: 0] += 1
    }
    return counter.values.filter({ $0 > 1 }).count
}
