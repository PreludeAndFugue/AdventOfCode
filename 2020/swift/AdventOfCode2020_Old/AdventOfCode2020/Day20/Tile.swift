//
//  Tile.swift
//  AdventOfCode2020
//
//  Created by gary on 22/12/2020.
//

import Foundation

final class Tile {
    enum Edge {
        case top(String)
        case bottom(String)
        case left(String)
        case right(String)
    }

    let n: Int
    let image: [String]

    
    init(n: Int, image: [String]) {
        self.n = n
        self.image = image
    }


    var topEdge: Edge {
        .top(image[0])
    }


    var bottomEdge: Edge {
        .bottom(image[-1])
    }


    var leftEdge: Edge {
        .left(image.map({ String($0.first!) }).joined())
    }


    var rightEdge: Edge {
        .right(image.map({ String($0.last!) }).joined())
    }
}
