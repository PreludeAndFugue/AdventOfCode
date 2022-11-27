//
//  Run9.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let PLAYER_COUNT = 459
private let MARBLE_COUNT = 100*71790

private let TEST_DATA: [(Int, Int)] = [
    (10, 1618),
    (13, 7999),
    (17, 1104),
    (21, 6111),
    (30, 5807)
]

func run9() {
//    test()
//    test1()
    main()
}


private func mainOld() {
    let game = Game(playerCount: PLAYER_COUNT, marbleCount: MARBLE_COUNT)
    game.run()
}


private func main() {
    let game = GameWithCircle(playerCount: PLAYER_COUNT, marbleCount: MARBLE_COUNT)
    game.run()
}


private func testOld() {
    for (playerCount, marbleCount) in TEST_DATA {
        let game = Game(playerCount: playerCount, marbleCount: marbleCount)
        game.run()
    }
}


private func test() {
    for (playerCount, marbleCount) in TEST_DATA {
        let game = GameWithCircle(playerCount: playerCount, marbleCount: marbleCount)
        game.run()
    }
}


private func test1_9() {
    let game = GameWithCircle(playerCount: 9, marbleCount: 25)
    game.run()
}
