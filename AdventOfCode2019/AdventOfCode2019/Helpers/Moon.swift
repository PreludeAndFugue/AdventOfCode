//
//  Moon.swift
//  AdventOfCode2019
//
//  Created by gary on 12/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Moon {
    private let name: String
    var position: Coordinate3
    var velocity: Coordinate3


    init(name: String, position: Coordinate3) {
        self.name = name
        self.position = position
        self.velocity = Coordinate3.origin
    }


    var potentialEnergy: Int {
        return abs(position.x) + abs(position.y) + abs(position.z)
    }


    var kineticEnergy: Int {
        return abs(velocity.x) + abs(velocity.y) + abs(velocity.z)
    }


    var totalEnergy: Int {
        return potentialEnergy * kineticEnergy
    }


    var state: [Int] {
        return [position.x, position.y, position.z, velocity.x, velocity.y, velocity.z]
    }


    func updatePosition() {
        position += velocity
    }


    func getGravity(for other: Moon) -> Coordinate3 {
        let x = getGravity(coord1: position.x, coord2: other.position.x)
        let y = getGravity(coord1: position.y, coord2: other.position.y)
        let z = getGravity(coord1: position.z, coord2: other.position.z)
        return Coordinate3(x: x, y: y, z: z)
    }


    func applyGravity(_ gravity: Coordinate3) {
        velocity += gravity
    }
}


extension Moon: CustomDebugStringConvertible {
    var debugDescription: String {
        return "\(name)(p: (\(position)), v: (\(velocity)))"
    }
}


private extension Moon {
    private func getGravity(coord1: Int, coord2: Int) -> Int {
        if coord1 < coord2 {
            return 1
        } else if coord1 == coord2 {
            return 0
        } else {
            return -1
        }
    }
}
