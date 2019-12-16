//
//  Problem15.swift
//  AdventOfCode2019
//
//  Created by gary on 15/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem15: Problem {
    private let file = "15/data15.txt"

    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 15, r1, r2)
    }
}


// MARK: - Private

private extension Problem15 {
    func part1() -> Int {
        let input = try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
        let controller = DroidController(memory: input)
        controller.run()
        let search = BreadthFirstSearch(
            elements: Array(controller.map),
            start: Coordinate.origin,
            goal: controller.oxygenSystemPosition!,
            getNeighbours: getNeighbours
        )
        let node = search.run()
        return node.path.count - 1
    }


    func getNeighbours(of coordinate: Coordinate, coordinates: [Coordinate]) -> [Coordinate] {
        let set = Set(coordinates)
        let candidates = [
            coordinate + Direction.up.vector,
            coordinate + Direction.down.vector,
            coordinate + Direction.left.vector,
            coordinate + Direction.right.vector
        ]
        return candidates.filter({ set.contains($0) })
    }
}
