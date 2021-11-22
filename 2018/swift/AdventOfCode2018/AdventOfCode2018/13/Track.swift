//
//  Track.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Track {
    private let carCharacters: Set<Character> = ["<", ">", "^", "v"]

    private let track: [[Character]]

    init(track: [[Character]]) {
        self.track = track
    }


    func part(at coordinate: Coordinate) -> Character {
        return track[coordinate.y][coordinate.x]
    }
}


extension Track: CustomDebugStringConvertible {
    var debugDescription: String {
        return stringify(track: self.track)
    }


    func display(with cars: [Car]) -> String {
        var trackCopy = track
        for car in cars {
            let coordinate = car.position
            if isCar(at: car.position, on: trackCopy) {
                trackCopy[coordinate.y][coordinate.x] = "X"
            } else {
                trackCopy[coordinate.y][coordinate.x] = car.chr
            }
        }
        return stringify(track: trackCopy)
    }


    private func stringify(track: [[Character]]) -> String {
        return track.map({ $0.map({ String($0) }).joined() }).joined(separator: "\n")
    }


    private func isCar(at coordinate: Coordinate, on track: [[Character]]) -> Bool {
        let chr = track[coordinate.y][coordinate.x]
        return carCharacters.contains(chr)
    }
}
