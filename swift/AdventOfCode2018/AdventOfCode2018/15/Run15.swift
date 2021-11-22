//
//  Run15.swift
//  AdventOfCode2018
//
//  Created by gary on 23/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

private let testMap1 = """
#######
#E..G.#
#...#.#
#.G.#G#
#######
"""


private let testMap2 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""


private let testMap3 = """
#######
#.E...#
#.....#
#...G.#
#######
"""


private let testMap4 = """
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
"""


private let testMap5 = """
##########
#........#
#........#
#.E.....G#
#........#
#........#
##########
"""


private let testMap6 = """
#######
#..G..#
#...#.#
#.#####
#...#E#
#.....#
#######
"""

func run15() {
    let game = Game15(mapString: testMap6)
    print(game.map)
    game.run()
}


func sortByReadingOrder<T: HasCoordinate>(item1: T, item2: T) -> Bool {
    if item1.coordinate.y < item2.coordinate.y {
        return true
    } else if item1.coordinate.y == item2.coordinate.y {
        return item1.coordinate.x < item2.coordinate.x
    }
    return false
}
