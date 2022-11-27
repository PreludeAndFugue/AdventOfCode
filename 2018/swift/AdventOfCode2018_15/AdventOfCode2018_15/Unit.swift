//
//  Unit.swift
//  AdventOfCode2018_15
//
//  Created by gary on 26/11/2022.
//

import Foundation

enum Unit {
    case empty
    case elf(Int)
    case goblin(Int)

    
    var hitPoints: Int {
        switch self {
        case .empty:
            return Int.max
        case .elf(let n):
            return n
        case .goblin(let n):
            return n
        }
    }


    var ch: String {
        switch self {
        case .empty:
            return "."
        case .elf:
            return "E"
        case .goblin:
            return "G"
        }
    }


    var isEmpty: Bool {
        switch self {
        case .empty:
            return true
        case .elf, .goblin:
            return false
        }
    }


    var isElf: Bool {
        switch self {
        case .elf:
            return true
        default:
            return false
        }
    }


    var isGoblin: Bool {
        switch self {
        case .goblin:
            return true
        default:
            return false
        }
    }


    func update(hitPoints: Int) -> Unit {
        switch self {
        case .empty:
            assertionFailure()
            return self
        case .goblin:
            return .goblin(hitPoints)
        case .elf:
            return .elf(hitPoints)
        }
    }
}


extension Unit: CustomDebugStringConvertible {
    var debugDescription: String {
        switch self {
        case .empty:
            return "."
        case .elf(let hitPoints):
            return "E(\(hitPoints))"
        case .goblin(let hitPoints):
            return "G(\(hitPoints))"
        }
    }
}
