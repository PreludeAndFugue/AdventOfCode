import Foundation

private let test = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

public func day02() {
    let testInstructions = parse(test)
    let url = Bundle.main.url(forResource: "day02", withExtension: "txt")!
    let string = try! String(contentsOf: url)
    let instructions = parse(string)

    tests(testInstructions)

    let (p1, p2) = solve(instructions)
    print(p1)
    print(p2)
}


private struct Instruction {
    let command: String
    let distance: Int

    init(_ string: String) {
        let parts = string.split(separator: " ")
        self.command = String(parts[0])
        self.distance = Int(parts[1])!
    }
}


private func parse(_ string: String) -> [Instruction] {
    string.trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: "\n")
        .map({ Instruction(String($0)) })
}


private func solve(_ instructions: [Instruction]) -> (Int, Int) {
    var depth1 = 0
    var depth2 = 0
    var totalDistance = 0
    var aim = 0
    for instruction in instructions {
        switch instruction.command {
        case "up":
            depth1 -= instruction.distance
            aim -= instruction.distance
        case "down":
            depth1 += instruction.distance
            aim += instruction.distance
        case "forward":
            totalDistance += instruction.distance
            depth2 += aim * instruction.distance
        default:
            fatalError()
        }
    }
    return (depth1 * totalDistance, depth2 * totalDistance)
}


private func tests(_ instructions: [Instruction]) {
    let (p1, p2) = solve(instructions)
    assert(p1 == 150)
    assert(p2 == 900)
}
