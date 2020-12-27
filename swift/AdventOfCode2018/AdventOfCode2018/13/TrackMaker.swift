//
//  TrackMaker.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

struct TrackMaker {

    private let carCharacters: Set<Character> = ["<", ">", "^", "v"]

    func make(fromString string: String) -> (Track, [Car]) {
        var parts: [[Character]] = []
        var cars: [Car] = []
        for (y, line) in string.split(separator: "\n").enumerated() {
            var row: [Character] = []
            for (x, chr) in String(line).enumerated() {
                if isCar(chr) {
                    let car = Car(x: x, y: y, character: chr)
                    cars.append(car)
                    row.append(car.trackPiece)
                } else {
                    row.append(chr)
                }
            }
            parts.append(row)
        }
        return (Track(track: parts), cars)
    }
}


private extension TrackMaker {
    func isCar(_ character: Character) -> Bool {
        return carCharacters.contains(character)
    }
}
