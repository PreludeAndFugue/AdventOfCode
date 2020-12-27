//
//  GameWithCircle.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class GameWithCircle {
    private let specialNo = 23
    private let marbleCount: Int
    private var circle: Circle
    private let players: Players


    init(playerCount: Int, marbleCount: Int) {
        self.circle = Circle(value: 0)
        self.marbleCount = marbleCount
        self.players = Players(playerCount: playerCount)
    }


    func run() {
        for i in 1...marbleCount {
            if i % 23 == 0 {
                specialMove(i)
            } else {
                standardMove(i)
            }
//            print(i, circle)
        }
        print(players.winner())
    }
}


// MARK: - Private

private extension GameWithCircle {
    func standardMove(_ marbleNo: Int) {
        circle.moveClockwise(n: 1)
        circle.insert(value: marbleNo)
    }


    func specialMove(_ marbleNo: Int) {
        players.add(marbleNo: marbleNo)
        circle.moveAntiClockwise(n: 7)
        let node = circle.remove()
        players.add(marbleNo: marbleNo, otherMarbleNo: node.value)
    }
}
