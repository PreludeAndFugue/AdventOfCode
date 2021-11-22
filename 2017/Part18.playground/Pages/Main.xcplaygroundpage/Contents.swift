//: Playground - noun: a place where people can play

import Cocoa


//let instructions = parseInput(input: TEST_INPUT)
let instructions = parseInput(input: Input.INPUT)
let p0 = Program(n: 0, instructions: instructions)
let p1 = Program(n: 1, instructions: instructions)

let coordinator = Coordinator(program0: p0, program1: p1)

coordinator.run()

print("done")
print(p1.finalSendCount)

