//
//  AStar.swift
//  AdventOfCode2018
//
//  Created by gary on 24/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class AStar {
    private var closedSet: Set<Coordinate>
    private var openSet: Set<Coordinate>
    private var cameFrom: [Coordinate: Coordinate]
    private var gScores: [Coordinate: Double]
    private var fScores: [Coordinate: Double]

    private let map: Map

    init(map: Map) {
        self.closedSet = []
        self.openSet = []
        self.cameFrom = [:]
        self.gScores = [:]
        self.fScores = [:]
        self.map = map
    }


    func run(start: Coordinate, goal: Coordinate) -> [Coordinate] {
        print("a star", start, goal)
        openSet.insert(start)
        gScores[start] = 0
        fScores[start] = heuristicCostEstimate(from: start, to: goal)
        while !openSet.isEmpty {
            let current = findLowestFScore(in: openSet, fScores: fScores)
            if current == goal {
                return reconstructPath(cameFrom: cameFrom, end: current)
            }
            openSet.remove(current)
            closedSet.insert(current)

            for neighbour in getValidNeighbourCoordinates(for: current, goal: goal) {
                if closedSet.contains(neighbour) {
                    continue
                }
                let tentativeGScore = gScores[current]! + heuristicCostEstimate(from: current, to: neighbour)

                if !openSet.contains(neighbour) {
                    openSet.insert(neighbour)
                } else if tentativeGScore >= gScores[neighbour, default: Double.infinity] {
                    continue
                }

                cameFrom[neighbour] = current
                gScores[neighbour] = tentativeGScore
                fScores[neighbour] = gScores[neighbour]! + heuristicCostEstimate(from: neighbour, to: goal)


                print("f scores", fScores)
                print("g scores", gScores)
                print("pair", current, neighbour, fScores[neighbour]!)
            }
        }
        return []
    }
}


private extension AStar {
    // Manhattan distance between MapCell coordinates
    func heuristicCostEstimate(from firstCoordinate: Coordinate, to endCoordinate: Coordinate) -> Double {
        return Double(firstCoordinate.manhattanDistance(to: endCoordinate)) + readingOrderCost(from: firstCoordinate, to: endCoordinate)
    }


    func findLowestFScoreOld(in items: Set<Coordinate>, fScores: [Coordinate: Double]) -> Coordinate {
        var currentScore = Double.infinity
        var currentItem: Coordinate? = nil
        for item in items {
            let score = fScores[item]!
            if score < currentScore {
                currentScore = score
                currentItem = item
            }
        }
        return currentItem!
    }


    func findLowestFScore(in items: Set<Coordinate>, fScores: [Coordinate: Double]) -> Coordinate {
        var currentScore = Double.infinity
        var currentItems: [Coordinate] = []
        for item in items {
            let score = fScores[item]!
            if score < currentScore {
                currentScore = score
                currentItems = [item]
            } else if score == currentScore {
                currentItems.append(item)
            }
        }
//        print("fScores", fScores)
        return Array(currentItems).sortByReadingOrder().first!
    }


    func getValidNeighbourCoordinates(for coordinate: Coordinate, goal: Coordinate) -> [Coordinate] {
        var results: [Coordinate] = []
        let mapCells = map.getNeighbours(of: coordinate)
        for mapCell in mapCells {
            if mapCell.coordinate == goal {
                results.append(mapCell.coordinate)
            } else if case .empty = mapCell.type {
                results.append(mapCell.coordinate)
            }
        }
        return results
    }


    func reconstructPath(cameFrom: [Coordinate: Coordinate], end: Coordinate) -> [Coordinate] {
        var totalPath = [end]
        var current = end
        while cameFrom.contains(where: { $0.key == current }) {
            current = cameFrom[current]!
            totalPath.append(current)
        }
        return totalPath
    }


    func readingOrderCost(from c1: Coordinate, to c2: Coordinate) -> Double {
        if c1.manhattanDistance(to: c2) != 1 { return 0 }
        let dx = c2.x - c1.x
        let dy = c2.y - c1.y
        switch (dx, dy) {
        case (0, -1): return 0
        case (-1, 0): return 0.3
        case (1, 0): return 0.6
        case (0, 1): return 0.9
        default: fatalError()
        }
    }
}
