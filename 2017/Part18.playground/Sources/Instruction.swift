import Foundation

public struct Instruction {
    let command: Command
    let value1: String
    let value2: String?

    public init(parts: [String]) {
        guard let command = Command(rawValue: parts[0]) else {
            fatalError("Unknown command: \(parts[0])")
        }
        self.command = command
        value1 = parts[1]
        if parts.count == 3 {
            value2 = parts[2]
        } else {
            value2 = nil
        }
    }
}
