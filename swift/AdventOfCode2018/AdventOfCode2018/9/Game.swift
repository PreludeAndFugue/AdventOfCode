//
//  Game.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Game {
    private let specialNo = 23

    private let marbleCount: Int

    private var circle: [Int] = [0]
    private var currentMarble = 0
    private let players: Players

    init(playerCount: Int, marbleCount: Int) {
        self.marbleCount = marbleCount
        self.players = Players(playerCount: playerCount)
    }


    func run() {
        reset()
        for i in 1...marbleCount {
            if i % 23 == 0 {
                specialMove(i)
            } else {
                normalMove(i)
            }
        }
        print(players.winner())
    }
}


// MARK: - Private

private extension Game {
    var currentMarbleIndex: Int {
        return circle.firstIndex(of: currentMarble)!
    }


    func getNextIndex() -> Int {
        let indexCount = circle.indices.count
        let newIndex = (currentMarbleIndex + 2) % indexCount
        if newIndex == 0 {
            return indexCount
        } else {
            return newIndex
        }
    }


    func normalMove(_ marbleNo: Int) {
        let nextIndex = getNextIndex()
        circle.insert(marbleNo, at: nextIndex)
        currentMarble = marbleNo
    }


    func specialMove(_ marbleNo: Int) {
        players.add(marbleNo: marbleNo)
        let indexCount = circle.indices.count
        var indexToRemove = (currentMarbleIndex - 7) % indexCount
        indexToRemove = indexToRemove < 0 ? indexToRemove + indexCount : indexToRemove
        let removedMarbleNo = circle.remove(at: indexToRemove)
        players.add(marbleNo: marbleNo, otherMarbleNo: removedMarbleNo)
        currentMarble = circle[indexToRemove]
    }


    func reset() {
        circle = [0]
        currentMarble = 0
    }
}
