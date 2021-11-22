//
//  Player.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Players {
    private let playerCount: Int
    private var playerScores: [Int: [Int]] = [:]

    init(playerCount: Int) {
        self.playerCount = playerCount
    }


    func getPlayerNo(fromMarbleNo marbleNo: Int) -> Int {
        let playerNo = marbleNo % playerCount
        if playerNo == 0 {
            return playerCount
        } else {
            return playerNo
        }
    }


    func add(marbleNo: Int) {
        let playerNo = getPlayerNo(fromMarbleNo: marbleNo)
        add(playerNo: playerNo, marbleNo: marbleNo)
    }


    func add(marbleNo: Int, otherMarbleNo: Int) {
        let playerNo = getPlayerNo(fromMarbleNo: marbleNo)
        add(playerNo: playerNo, marbleNo: otherMarbleNo)
    }


    func winner() -> (Int, Int) {
        let item = playerScores.mapValues({ $0.reduce(0, +) }).sorted(by: { $0.value > $1.value }).first!
        return (item.key, item.value)
    }
}


// MARK: - Private

private extension Players {
    func add(playerNo: Int, marbleNo: Int) {
        if var scores = playerScores[playerNo] {
            scores.append(marbleNo)
            playerScores[playerNo] = scores
        } else {
            playerScores[playerNo] = [marbleNo]
        }
    }
}


// MARK: - CustomDebugStringConvertible

extension Players: CustomDebugStringConvertible {
    var debugDescription: String {
        return playerScores.debugDescription
    }
}
