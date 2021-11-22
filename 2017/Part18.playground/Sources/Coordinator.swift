import Foundation

public class Coordinator {

    let program0: Program
    let program1: Program

    public init(program0: Program, program1: Program) {
        self.program0 = program0
        self.program1 = program1
        program0.delegate = self
        program1.delegate = self
    }


    public func run() {
        while canRun() {
            program0.run()
            program1.run()
            print("done cycle", program0.queueLength, program1.queueLength)
        }
    }


    private func canRun() -> Bool {
        return program0.canRun() || program1.canRun()
    }
}


extension Coordinator: ProgramDelegate {
    public func programSend(number: Int, value: Int) {
        if number == 0 {
            program1.addToQueue(value: value)
        } else {
            program0.addToQueue(value: value)
        }
    }
}
