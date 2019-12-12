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


    func updatePosition() {
        position = position + velocity
    }
}


extension Moon: CustomDebugStringConvertible {
    var debugDescription: String {
        return "\(name)(p: \(position), v: \(velocity))"
    }
}
