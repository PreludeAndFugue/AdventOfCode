//
//  FullImage.swift
//  AdventOfCode2020
//
//  Created by gary on 25/12/2020.
//

final class FullImage {
    private let tiles: [[Tile]]

    init(neighbourMap: [Int: [Tile]]) {
        self.tiles = FullImage.makeTiles(from: neighbourMap)
    }


    func image() -> String {
        var rows: [String] = []
        for row in tiles {
            let height = row[0].image.count
            var parts: [String] = []
            for i in 0..<height {
                let part = row.map({ $0.image[i] }).joined(separator: " ")
                parts.append(part)
            }
            rows.append(parts.joined(separator: "\n"))
        }
        return rows.joined(separator: "\n\n")
    }


    func trimmedImage(separator: String = "\n") -> String {
        var rows: [String] = []
        for row in tiles {
            let height = row[0].image.count
            var parts: [String] = []
            for i in 1..<(height - 1) {
                let part = row.map({ trimmed(row: i, image: $0.image) }).joined()
                parts.append(part)
            }
            rows.append(parts.joined(separator: separator))
        }
        return rows.joined(separator: separator)
    }


    func trimmedImageAllOrientations(separator: String = "\n") -> [String] {
        let original = trimmedImage(separator: separator)
        let elements = trimmedImage(separator: "\n")
            .components(separatedBy: "\n")
            .map({ Array($0) })
        let flippedElements = elements.reversed()

        let r90 = elements.reversed().transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let r180 = elements.reversed().transposed().reversed().transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let r270 = elements.transposed().reversed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let flipped = flippedElements
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let flippedR90 = flippedElements.reversed().transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let flippedR180 = flippedElements.reversed().transposed().reversed().transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)
        let flipped270 = flippedElements.transposed().reversed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
            .joined(separator: separator)

        return [
            original,
            r90, r180, r270,
            flipped,
            flippedR90, flippedR180, flipped270
        ]
    }
}


// MARK: - Private

private extension FullImage {
    func trimmed(row: Int, image: [String]) -> String {
        let s = image[row]
        let start = s.index(after: s.startIndex)
        let end = s.index(before: s.endIndex)
        return String(s[start..<end])
    }
}


// MARK: - Private static

private extension FullImage {
    private static func makeTiles(from neighbourMap: [Int: [Tile]]) -> [[Tile]] {
        let coordMap = makeCoordMap(from: neighbourMap)
        let reverseCoordMap = makeReverseCoordMap(from: coordMap)
        let tileMap = makeTileMap(from: neighbourMap)
        let xs = Set(coordMap.map({ $0.value.x })).sorted()
        let ys = Set(coordMap.map({ $0.value.y })).sorted()
        var tiles: [[Tile]] = []
        for y in ys {
            var row: [Tile] = []
            for x in xs {
                let c = Coordinate(x: x, y: y)
                let n = reverseCoordMap[c]!
                let tile = tileMap[n]!
                row.append(tile)
            }
            tiles.append(row)
        }
        return tiles
    }


    private static func makeCoordMap(from neighbourMap: [Int: [Tile]]) -> [Int: Coordinate] {
        var coordMap: [Int: Coordinate] = [:]
        let t0 = neighbourMap.first!.value[0]
        coordMap[t0.n] = Coordinate(x: 0, y: 0)
        var toCheck = [t0]
        var seen: Set<Int> = []
        while !toCheck.isEmpty {
            let tile = toCheck.removeFirst()
            for n in neighbourMap[tile.n]! {
                if seen.contains(n.n) { continue }
                let nCoord = coordMap[tile.n]! + tile.offset(of: n)
                coordMap[n.n] = nCoord
                seen.insert(n.n)
                toCheck.append(n)
            }
        }
        return coordMap
    }


    private static func makeReverseCoordMap(from coordMap: [Int: Coordinate]) -> [Coordinate: Int] {
        var reverseCoordMap: [Coordinate: Int] = [:]
        for (k, v) in coordMap {
            reverseCoordMap[v] = k
        }
        return reverseCoordMap
    }


    private static func makeTileMap(from neighbourMap: [Int: [Tile]]) -> [Int: Tile] {
        var map: [Int: Tile] = [:]
        for tiles in neighbourMap.values {
            for tile in tiles {
                map[tile.n] = tile
            }
        }
        return map
    }
}
