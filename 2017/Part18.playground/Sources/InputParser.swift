import Foundation

public func parseInput(input: String) -> [Instruction] {
    var instructions: [Instruction] = []
    let rows = input.split(separator: "\n")
    for row in rows {
        let parts = row.split(separator: " ").map{ String(describing: $0) }
        let instruction = Instruction(parts: parts)
        instructions.append(instruction)
    }
    return instructions
}
