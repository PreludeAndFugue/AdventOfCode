//
//  Data12.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

protocol Data12Protocol {
    var initialState: String { get }
    var rules: String { get }
}


extension Data12Protocol {
    func makeRulesOld(_ string: String) -> [Rule12] {
        return string.split(separator: "\n").map({ Rule12(string: String($0)) })
    }


    func makeRules(_ string: String) -> Rules12 {
        return Rules12(string: string)
    }
}


struct Data12: Data12Protocol {
    let initialState = "###..#...####.#..###.....####.######.....##.#####.##.##..###....#....##...##...##.#..###..#.#...#..#"

    let rules = """
        .###. => .
        ..#.. => .
        .#### => .
        .##.. => #
        #.#.# => .
        ..#.# => #
        #.##. => #
        #...# => #
        ..... => .
        ##..# => #
        .#.#. => .
        ..##. => #
        ##.#. => .
        ###.. => .
        .#... => #
        ..### => .
        #..## => .
        ...#. => .
        ###.# => #
        .##.# => .
        .#.## => .
        ....# => .
        ##### => .
        #.#.. => #
        ...## => #
        #.... => .
        #.### => #
        ##... => #
        .#..# => .
        ####. => .
        #..#. => #
        ##.## => #
        """
}

struct Data12Test: Data12Protocol {
    let initialState = "#..#.#..##......###...###"
    let rules = """
        ...## => #
        ..#.. => #
        .#... => #
        .#.#. => #
        .#.## => #
        .##.. => #
        .#### => #
        #.#.# => #
        #.### => #
        ##.#. => #
        ##.## => #
        ###.. => #
        ###.# => #
        ####. => #
        """
}
