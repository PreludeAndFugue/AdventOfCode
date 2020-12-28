//
//  Problem18Helper.swift
//  AdventOfCode2019
//
//  Created by gary on 22/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem18Helper {
    struct Location: Hashable, CustomDebugStringConvertible {
        enum LocationType {
            case path
            case door(String)
            case key(String)
            case me

            var isMe: Bool {
                switch self {
                case .me: return true
                default: return false
                }
            }

            var isDoor: Bool {
                switch self {
                case .door: return true
                default: return false
                }
            }

            var isKey: Bool {
                switch self {
                case .key: return true
                default: return false
                }
            }

            var name: String? {
                switch self {
                case .door(let name): return name
                case .key(let name): return name
                case .me: return "0"
                default: return nil
                }
            }
        }

        let coordinate: Coordinate
        let type: LocationType


        func move(_ direction: Direction) -> Location {
            return Location(
                coordinate: coordinate + direction.vector,
                type: type
            )
        }


        func hash(into hasher: inout Hasher) {
            hasher.combine(coordinate)
        }


        static func == (lhs: Location, rhs: Location) -> Bool {
            return lhs.coordinate == rhs.coordinate
        }


        var debugDescription: String {
            return "\(type)\(coordinate)"
        }
    }


    struct Edge: Hashable, CustomDebugStringConvertible {
        let key1: String
        let key2: String
        let distance: Int
        let doors: Set<String>

        init(path: [Location]) {
//            print(path)
            self.key1 = path.first?.type.name ?? "XXX"
            self.key2 = path.last?.type.name ?? "XXX"
            self.distance = path.count - 1
            self.doors = Set(path.filter({ $0.type.isDoor }).compactMap({ $0.type.name?.lowercased() }))
        }

        var debugDescription: String {
            let doorString = doors.joined()
            return "Edge(\(key1), \(key2), \(distance), {\(doorString)})"
        }
    }


    private let mapString: String


    init(mapString: String) {
        self.mapString = mapString
    }


    func makeEdges() -> [Edge] {
        let map = makeMap()
        let start = map.filter({ $0.type.isMe }).first!
        let keys = map.filter({ $0.type.isKey }).sorted(by: { $0.type.name! < $1.type.name! })
        let locations = [start] + keys

        var seenPairs: Set<String> = []
        var edges: [Edge] = []
        for combinations in locations.combinations(r: 2) {
            let c1 = combinations[0]
            let c2 = combinations[1]
            let name1 = c1.type.name!
            let name2 = c2.type.name!
            print(name1, name2)
            let seen1 = "\(name1)\(name2)"
            let seen2 = "\(name2)\(name1)"
            if seenPairs.contains(seen1) || seenPairs.contains(seen2) {
                print("alread seen", seen1, seen2)
                continue
            }
            let path = pathBetween(start: c1, goal: c2, elements: map)
            let newEdges = makeEdges(from: path)
            for edge in newEdges {
                seenPairs.insert("\(edge.key1)\(edge.key2)")
                seenPairs.insert("\(edge.key2)\(edge.key1)")
            }
            edges.append(contentsOf: newEdges)
        }
        return edges
    }
}


// MARK: - Private

private extension Problem18Helper {
    private func makeMap() -> [Location] {
        var locations: Set<Location> = []
        var row = 0
        var column = 0
        for chr in mapString {
            if chr == "." {
                let coordinate = Coordinate(x: column, y: row)
                let location = Location(coordinate: coordinate, type: .path)
                locations.insert(location)
                column += 1
            } else if chr == "\n" {
                row += 1
                column = 0
            } else if chr == "#" {
                column += 1
            } else if chr.isUppercase {
                let coordinate = Coordinate(x: column, y: row)
                let location = Location(coordinate: coordinate, type: .door(String(chr)))
                locations.insert(location)
                column += 1
            } else if chr.isLowercase {
                let coordinate = Coordinate(x: column, y: row)
                let location = Location(coordinate: coordinate, type: .key(String(chr)))
                locations.insert(location)
                column += 1
            } else if chr == "@" {
                let coordinate = Coordinate(x: column, y: row)
                let location = Location(coordinate: coordinate, type: .me)
                locations.insert(location)
                column += 1
            } else {
                // new empty
                column += 1
//                fatalError()
            }
        }
        return Array(locations)
    }


    private func pathBetween(start: Location, goal: Location, elements: [Location]) -> [Location] {
        let search = BreadthFirstSearch<Location>(
            elements: elements,
            start: start,
            goal: goal,
            getNeighbours: getNeighbours
        )
        return search.run().path
    }


    private func getNeighbours(of location: Location, locations: [Location]) -> [Location] {
        let set = Set(locations)
        let candidates = [
            location.move(.up),
            location.move(.down),
            location.move(.left),
            location.move(.right)
        ]
        return Array(set.intersection(candidates))
    }


    private func makeEdges(from path: [Location]) -> [Edge] {
        var edges: [Edge] = []
//        print(path)
        var keyIndexes: [Int] = []
        for (i, location) in path.enumerated() {
            if location.type.isKey || location.type.isMe {
                keyIndexes.append(i)
            }
        }
//        print("keyIndexes", keyIndexes)
        for (i, j) in zip(keyIndexes, keyIndexes[1...]) {
            let subPath = Array(path[i...j])
            let edge = Edge(path: subPath)
            edges.append(edge)
        }
        return edges
    }


    private func isShortest(path: [Location]) -> Bool {
        let keyCount = path.filter({ $0.type.isKey || $0.type.isMe }).count
        return keyCount <= 2
    }
}
