//
//  Problem15.swift
//  AdventOfCode2019
//
//  Created by gary on 15/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

///
/// Problem 15
///
/// Algorithm for exploring the full maze for part 2
/// ------------------------------------------------
///
/// * Choose the initial cell, mark it as visited and push it to the stack
/// * While the stack is not empty
///     * Pop a cell from the stack and make it a current cell
///     * If the current cell has any neighbours which have not been visited
///         * Push the current cell to the stack
///         * Choose one of the unvisited neighbours
///         * Remove the wall between the current cell and the chosen cell
///         * Mark the chosen cell as visited and push it to the stack
///
/// Another idea for exploring the full maze for part 2
/// ---------------------------------------------------
///
/// The droid controller uses a wall follower algorithm to find the oxygen
/// system, then stops. Instead, if we don't stop at the oxygen system, but
/// continue until we return to the start point, then I think we will have
/// mapped all the maze.
///
final class Problem15: Problem {
    private let file = "15/data15.txt"
    private lazy var input = {
        try! String(contentsOfFile: path + file).makeIntegers(separator: ",")
    }()


    func run() {
        let r1 = part1()
        let r2 = part2()
        printResults(number: 15, r1, r2)
    }
}


// MARK: - Private

private extension Problem15 {
    private func part1() -> Int {
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


    private func part2() -> Int {
        let controller = DroidController(memory: input)
        let (start, map) = controller.getCoords()
        let oxygenSpread = mapOxygenSpread(start: start, map: map)

        draw(map: map, oxygenSpread: oxygenSpread)

        return oxygenSpread.count - 1
    }


    private func getNeighbours(of coordinate: Coordinate, coordinates: [Coordinate]) -> [Coordinate] {
        let set = Set(coordinates)
        let candidates = [
            coordinate + Direction.up.vector,
            coordinate + Direction.down.vector,
            coordinate + Direction.left.vector,
            coordinate + Direction.right.vector
        ]
        return candidates.filter({ set.contains($0) })
    }


    private func mapOxygenSpread(start: Coordinate, map: Set<Coordinate>) -> [[Coordinate]] {
        var toSearch = [start]
        var searched: Set<Coordinate> = []
        var result: [[Coordinate]] = []
        while !toSearch.isEmpty {
            var allNeighbours: [Coordinate] = []
//            print(toSearch)
            for coord in toSearch {
                let neighbours = getNeighbours(of: coord, coordinates: Array(map))
                allNeighbours.append(contentsOf: neighbours)
                searched.insert(coord)
            }
            toSearch = Array(Set(allNeighbours).subtracting(searched))
            result.append(toSearch)
        }
        return result
    }


    private func draw(map: Set<Coordinate>, oxygenSpread: [[Coordinate]]) {
        let screen = MazeScreen(map: map, oxygenSpread: oxygenSpread)
        screen.draw()
    }
}
