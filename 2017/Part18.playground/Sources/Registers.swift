import Foundation

public class Registers {

    private var registers: Dictionary<String, Int> = [:]

    public init(n: Int) {
        registers["p"] = n
    }


    public func get(register: String) -> Int {
        if let registerValue = registers[register] {
            return registerValue
        } else {
            registers[register] = 0
            return 0
        }
    }


    public func set(register: String, value: Int) {
        registers[register] = value
    }
}


extension Registers: CustomDebugStringConvertible {
    public var debugDescription: String {
        return String(describing: registers)
    }
}
