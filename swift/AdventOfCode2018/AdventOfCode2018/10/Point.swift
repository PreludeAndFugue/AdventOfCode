//
//  Point.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Point {
    var x: Int
    var y: Int
    var u: Int
    var v: Int


    init(x: Int, y: Int, u: Int, v: Int) {
        self.x = x
        self.y = y
        self.u = u
        self.v = v
    }


    func move() {
        x += u
        y += v
    }
}


// MARK: - CustomDebugStringConvertible

extension Point: CustomDebugStringConvertible {
    var debugDescription: String {
        return "Point(x: \(self.x), y: \(self.y), u: \(self.u), v: \(self.v))"
    }
}
