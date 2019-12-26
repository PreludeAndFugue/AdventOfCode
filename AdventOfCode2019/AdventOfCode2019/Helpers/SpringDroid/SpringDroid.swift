//
//  SpringDroid.swift
//  AdventOfCode2019
//
//  Created by gary on 26/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class SpringDroid {
    enum EndState {
        case done
        case fall(Int)
    }


    private var t = false
    private var j = false
    private var position = 0
    private let hull: [Bool]
    private var state: EndState = .done


    init(hull: [Bool]) {
        self.hull = hull
    }


    func run() -> EndState {
        while true {
            guard let (a, b, c, d) = getHullValues() else {
                break
            }
            test(a: a, b: b, c: c, d: d)
            if j {
                position += 4
            } else {
                position += 1
            }
            if hull[position] == false {
                state = .fall(position)
                break
            }
        }
        return state
    }


    func test(a: Bool, b: Bool, c: Bool, d: Bool) {
        not(x: a, y: &j)
    }
}


// MARK: - Private

private extension SpringDroid {
    private func and(x: Bool, y: inout Bool) {
        y = x && y
    }


    private func or(x: Bool, y: inout Bool) {
        y = x || y
    }


    private func not(x: Bool, y: inout Bool) {
        y = !x
    }


    private func getHullValues() -> (Bool, Bool, Bool, Bool)? {
        if position + 4 >= hull.count {
            return nil
        }
        return (hull[position + 1], hull[position + 2], hull[position + 3], hull[position + 4])
    }
}
