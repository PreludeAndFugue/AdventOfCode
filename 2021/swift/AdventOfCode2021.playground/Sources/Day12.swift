import Foundation

private typealias Map12 = [String: [String]]

private let test1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

private let test2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

private let test3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


struct Path: Hashable {
    let nodes: [String]

    var isEnded: Bool {
        nodes.contains("end")
    }


    func extend(node: String) -> Path? {
        if node.allSatisfy({ $0.isLowercase }) {
            if !nodes.contains(node) {
                var nodes = nodes
                nodes.append(node)
                return Path(nodes: nodes)
            } else {
                return nil
            }
        } else {
            var nodes = nodes
            nodes.append(node)
            return Path(nodes: nodes)
        }
    }


    func contains(node: String) -> Bool {
        nodes.contains(node)
    }
}


private func parse(string: String) -> Map12 {
    var map: Map12 = [:]
    let lines = string.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "\n")
    for line in lines {
        let parts = line.split(separator: "-").map({ String($0) })
        let from = parts.first!
        let to = parts.last!
        assert(from != to)
        if to != "start" {
            map[from, default: []].append(to)
        }
        if from != "start" {
            map[to, default: []].append(from)
        }
    }
    map.removeValue(forKey: "end")
    return map
}


private func findPaths(map: Map12) -> [Path] {
    var seen: Set<Path> = []
    var toCheck = [Path(nodes: ["start"])]
    var result: [Path] = []
    while !toCheck.isEmpty {
        let path = toCheck.popLast()!
        if seen.contains(path) {
            continue
        }
        seen.insert(path)
        if path.isEnded {
            result.append(path)
        } else {
            toCheck.append(contentsOf: nextPaths(path: path, map: map))
        }
    }
    return result
}


private func nextPaths(path: Path, map: Map12) -> [Path] {
    let end = path.nodes.last!
    return map[end, default: []].compactMap({ path.extend(node: $0) })
}


public func day12() {
    let testInput1 = parse(string: test1)
    let testInput2 = parse(string: test2)
    let testInput3 = parse(string: test3)
    let map = parse(string: read("day12"))

    let t1 = findPaths(map: testInput1)
    assert(t1.count == 10, "assertion 1")
    let t2 = findPaths(map: testInput2)
    assert(t2.count == 19, "assertion 2")
    let t3 = findPaths(map: testInput3)
    assert(t3.count == 226, "assertion 3")

    let p1 = findPaths(map: map).count
    print("Part 1: \(p1)")
}
