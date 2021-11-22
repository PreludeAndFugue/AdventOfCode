//
//  Runner13.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

final class Runner13 {
    private let trackMaker = TrackMaker()

    private let track: Track
    private var cars: [Car]

    init(string: String) {
        let (track, cars) = trackMaker.make(fromString: string)
        self.track = track
        self.cars = cars
    }


    func runUntilCrash() -> Coordinate {
        while true {
            if case let .yes(position) = tick() {
                return position
            }
        }
    }


    func runUntilLastCar() -> Coordinate {
        while true {
            if cars.count == 1 {
                let car = cars.first!
                return car.position
            }
            tickWithCrashes()
        }
    }
}


// MARK: - Private

extension Runner13 {
    enum CrashState {
        case yes(Coordinate)
        case no
    }


    func tick() -> CrashState {
        let sortedCars = cars.sorted(by: carSorter)
        for car in sortedCars {
            let nextPosition = car.nextPosition
            let nextTrackPart = track.part(at: nextPosition)
            car.move(nextTrackPart: nextTrackPart)
            if case let .yes(position) = isCrash() {
                return .yes(position)
            }
        }
        return .no
    }


    func tickWithCrashes() {
        let sortedCars = cars.sorted(by: carSorter)
        for car in sortedCars {
            let nextPosition = car.nextPosition
            let nextTrackPart = track.part(at: nextPosition)
            car.move(nextTrackPart: nextTrackPart)
            if case let .yes(position) = isCrash() {
                removeCars(at: position)
            }
        }
    }


    func isCrash() -> CrashState {
        var carPositions: [Coordinate: Int] = [:]
        for car in cars {
            let position = car.position
            if let count = carPositions[position] {
                carPositions[position] = count + 1
            } else {
                carPositions[position] = 1
            }
        }
        for (position, count) in carPositions {
            if count > 1 {
                return .yes(position)
            }
        }
        return .no
    }


    func removeCars(at coordinate: Coordinate) {
        var newCars: [Car] = []
        for car in cars {
            if car.position != coordinate {
                newCars.append(car)
            }
        }
        cars = newCars
    }


    func carSorter(car1: Car, car2: Car) -> Bool {
        if car1.position.y < car2.position.y {
            return true
        } else if car1.position.y == car2.position.y {
            return car1.position.x < car2.position.x
        } else {
            return false
        }
    }


    func positions(of cars: [Car]) -> [(Int, Int)] {
        return cars.map({ ($0.position.x, $0.position.y) })
    }
}
