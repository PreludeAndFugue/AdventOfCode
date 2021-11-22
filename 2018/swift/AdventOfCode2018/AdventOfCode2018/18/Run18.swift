//
//  Run18.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

func run18() {
    test18a()
//    main18a()
    main18b()
}


private func main18a() {
    let game = Game18(data: data18)
    game.run(steps: 10)
    print(game.resourceValue)
}


private func main18b() {
    let total = 1_000_000_000

//    let x1 = 537
//    let x2 = 564
//    let diff = x2 - x1
//    let y1 = (total - x1) % diff
//    print(x1, x2, diff, y1)

    let game = Game18(data: data18)
    var patterns: [String: Int] = [:]
    var startRepeat: Int = 0
    var endRepeat: Int = 0
    var minute = 1
    while true {
        game.step()
        let pattern = game.debugDescription
        if minute > 530 {
            print(minute, game.resourceValue)
        }
        if let time = patterns[pattern] {
            print("pattern repeated", minute, time)
            startRepeat = time
            endRepeat = minute
            break
        } else {
            patterns[pattern] = minute
        }
        minute += 1
    }


    print(startRepeat, endRepeat)
    let diff = endRepeat - startRepeat
    print(diff)

    var mainCounter = endRepeat
    while mainCounter <= total {
        mainCounter += diff
    }
    print(mainCounter)

    print(endRepeat - (mainCounter - total))
}


private func test18a() {
    let game = Game18(data: test18)
    game.run(steps: 10)
    assert(game.debugDescription == test18Result)
    assert(game.resourceValue == 1147)
}
