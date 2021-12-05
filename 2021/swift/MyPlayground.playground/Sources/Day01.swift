import Foundation


let testDepths = """
199
200
208
210
200
207
240
269
260
263
"""
.trimmingCharacters(in: .whitespacesAndNewlines)
.split(separator: "\n")
.compactMap({ Int($0) })



public func day01() {
    tests(depths: testDepths)

    let depths = getDepths()

    let p1 = calculate(depths: depths, diff: 1)
    print(p1)

    let p2 = calculate(depths: depths, diff: 3)
    print(p2)
}


// MARK: - Private


func getDepths() -> [Int] {
    let url = Bundle.main.url(forResource: "day01", withExtension: "txt")!
    return try! String(contentsOf: url)
        .trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
        .compactMap({ Int($0) })
}


func calculate(depths: [Int], diff: Int) -> Int {
    zip(depths, depths[diff...])
        .map({ $0.1 > $0.0 ? 1 : 0 })
        .reduce(0, +)
}


func tests(depths: [Int]) {
    assert(calculate(depths: depths, diff: 1) == 7)
    assert(calculate(depths: depths, diff: 3) == 5)
}
