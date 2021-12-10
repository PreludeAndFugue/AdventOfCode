import Foundation

typealias Map = [Point: Int]

private let test = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


public func day09() {
    let testMap = parse(test)
    let map = parse(read("day09"))

    let t1 = part1(map: testMap)
    assert(t1 == 15)

    let p1 = part1(map: map)
    print(p1)

    let t2 = part2_09(map: testMap)
    assert(t2 == 1134)

    let p2 = part2_09(map: map)
    print(p2)
}


private func parse(_ string: String) -> Map {
    let lines = string.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n")
    var map: [Point: Int] = [:]
    for (row, line) in lines.enumerated() {
        for (col, ch) in line.enumerated() {
            let point = Point(x: row, y: col)
            let n = Int(String(ch))!
            map[point] = n
        }
    }
    return map
}


private func neighbours(point: Point, map: Map) -> [Point] {
    let others = [
        Point(x: point.x - 1, y: point.y), Point(x: point.x + 1, y: point.y),
        Point(x: point.x, y: point.y - 1), Point(x: point.x, y: point.y + 1)
    ]
    var ns: [Point] = []
    for p in others {
        if map[p] != nil {
            ns.append(p)
        }
    }
    return ns
}


private func isMinimum(point: Point, map: Map) -> Bool {
    let ns = neighbours(point: point, map: map)
    let heights = ns.map({ map[$0]! })
    let height = map[point]!
    if height == 9 {
        return false
    }
    for h in heights {
        if h < height {
            return false
        }
    }
    return true
}


private func basin(point: Point, map: Map) -> [Point] {
    var toCheck = [point]
    var seen: Set<Point> = []
    var basin: [Point] = []
    while !toCheck.isEmpty {
        let p = toCheck.removeFirst()
        guard !seen.contains(p) else { continue }
        let h = map[p]!
        if h < 9 {
            basin.append(p)
            toCheck.append(contentsOf: neighbours(point: p, map: map))
            seen.insert(p)
        }
    }
    return basin
}


private func part1(map: Map) -> Int {
    map.keys.filter({ isMinimum(point: $0, map: map) })
        .map({ map[$0]! + 1 })
        .reduce(0, +)
}


private func part2_09(map: Map) -> Int {
    let minimums = map.keys.filter({ isMinimum(point: $0, map: map) })
    var basins: [[Point]] = []
    for m in minimums {
        let b = basin(point: m, map: map)
        basins.append(b)
    }
    return basins.map({ $0.count }).sorted().reversed()[..<3].reduce(1, *)
}
