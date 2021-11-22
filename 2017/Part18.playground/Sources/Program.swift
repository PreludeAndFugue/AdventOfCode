import Foundation


public protocol ProgramDelegate {
    func programSend(number: Int, value: Int)
}


public class Program {

    public enum State {
        case running
        case waiting
    }

    typealias BinaryIntFunction = (Int, Int) -> Int

    public var delegate: ProgramDelegate?
    public var state = State.running

    private let n: Int
    private var position = 0
    private let instructions: [Instruction]
    private let registers: Registers
    private var queue: [Int] = []
    private var sendCount = 0

    public init(n: Int, instructions: [Instruction]) {
        self.n = n
        self.instructions = instructions
        self.registers = Registers(n: n)
    }


    public var finalSendCount: Int {
        return sendCount
    }


    public var queueLength: Int {
        return queue.count
    }


    public func addToQueue(value: Int) {
        queue.append(value)
    }


    public func canRun() -> Bool {
//        print("Program(\(n)), can run", state, queue.count)
        return state == .running || queue.count > 0
    }


    func run() {
        while state == .running || queue.count > 0 {

//            print("Program(\(n))", state, position, registers, queue)

            if position < 0 || position >= instructions.count {
                fatalError("Program \(n), position (\(position)) out of bounds.")
            }
            let instruction = instructions[position]
            switch instruction.command {
            case .add:
                guard let value2 = instruction.value2 else { fatalError("Invalid instruction") }
                add(register: instruction.value1, value: value2)
            case .jgz:
                guard let value2 = instruction.value2 else { fatalError("Invalid instruction") }
                jgz(register: instruction.value1, value: value2)
            case .mod:
                guard let value2 = instruction.value2 else { fatalError("Invalid instruction") }
                mod(register: instruction.value1, value: value2)
            case .mul:
                guard let value2 = instruction.value2 else { fatalError("Invalid instruction") }
                mul(register: instruction.value1, value: value2)
            case .rcv:
                rcv(register: instruction.value1)
            case .set:
                guard let value2 = instruction.value2 else { fatalError("Invalid instruction") }
                set(register: instruction.value1, value: value2)
            case .snd:
                snd(value: instruction.value1)
            }
        }
    }


    func next() {
        position += 1
    }


    private func add(register: String, value: String) {
        helper(register: register, value: value, binaryFunc: +)
        next()
    }


    private func jgz(register: String, value: String) {
//        let registerValue = registers.get(register: register)
        let registerValue = getInt(fromValue: register)
        if registerValue <= 0 {
            next()
            return
        }
        let jumpValue = getInt(fromValue: value)
        position += jumpValue
    }


    private func mod(register: String, value: String) {
        helper(register: register, value: value, binaryFunc: %)
        next()
    }


    private func mul(register: String, value: String) {
        helper(register: register, value: value, binaryFunc: *)
        next()
    }


    private func rcv(register: String) {
        if queue.count > 0 {
            let value = queue.removeFirst()
//            print("receive", register, value)
            registers.set(register: register, value: value)
            state = .running
            next()
        } else {
//            print("receive, empty queue")
            state = .waiting
        }
    }


    private func set(register: String, value: String) {
        let newValue = getInt(fromValue: value)
        registers.set(register: register, value: newValue)
        next()
    }


    private func snd(value: String) {
//        print("send", value)
        let valueToSend = getInt(fromValue: value)
        delegate?.programSend(number: n, value: valueToSend)
        sendCount += 1
        next()
    }


    private func helper(register: String, value: String, binaryFunc: BinaryIntFunction) {
        let registerValue = registers.get(register: register)
        let changeValue = getInt(fromValue: value)
        let newValue = binaryFunc(registerValue, changeValue)
        registers.set(register: register, value: newValue)
    }


    private func getInt(fromValue value: String) -> Int {
        if let value = Int(value) {
            return value
        } else {
            return registers.get(register: value)
        }
    }
}

