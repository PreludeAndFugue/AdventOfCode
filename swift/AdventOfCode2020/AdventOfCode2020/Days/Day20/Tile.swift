//
//  Tile.swift
//  AdventOfCode2020
//
//  Created by gary on 22/12/2020.
//

import Foundation

final class Tile {
    enum Rotation {
        case R90
        case R180
        case R270
    }

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


    convenience init(string: String) {
        let parts = string.components(separatedBy: ":\n")
        assert(parts.count == 2)
        let n = Int(parts[0].trimmingCharacters(in: CharacterSet(charactersIn: "Tile ")))!
        let image = parts[1].components(separatedBy: "\n").map({ String($0) })
        self.init(n: n, image: image)
    }


    var topEdge: Edge {
        .top(image.first!)
    }


    var bottomEdge: Edge {
        .bottom(image.last!)
    }


    var leftEdge: Edge {
        .left(image.map({ String($0.first!) }).joined())
    }


    var rightEdge: Edge {
        .right(image.map({ String($0.last!) }).joined())
    }


    /// Checks if another tile has a matching edge.
    ///
    /// - Parameter other: The other tile.
    /// - Returns: The pair of matching edges
    func hasMatchingEdges(with other: Tile) -> (Edge, Edge)? {
        if topEdge.content == other.bottomEdge.content {
            return (topEdge, other.bottomEdge)
        } else if bottomEdge.content == other.topEdge.content {
            return (bottomEdge, other.topEdge)
        } else if leftEdge.content == other.rightEdge.content {
            return (leftEdge, other.rightEdge)
        } else if rightEdge.content == other.leftEdge.content {
            return (rightEdge, other.leftEdge)
        } else {
            return nil
        }
    }


    func allOrientations() -> [Tile] {
        return [
            self,
            self.rotated(.R90),
            self.rotated(.R180),
            self.rotated(.R270),
            self.flipped(),
            self.flipped().rotated(.R90),
            self.flipped().rotated(.R180),
            self.flipped().rotated(.R270)
        ]
    }


    func offset(of other: Tile) -> Coordinate {
        let (e1, e2) = hasMatchingEdges(with: other)!
        switch (e1, e2) {
        case (.top, .bottom):
            return Coordinate(x: 0, y: -1)
        case (.bottom, .top):
            return Coordinate(x: 0, y: 1)
        case (.left, .right):
            return Coordinate(x: -1, y: 0)
        case (.right, .left):
            return Coordinate(x: 1, y: 0)
        default:
            fatalError()
        }
    }


    private func rotated(_ rotation: Rotation) -> Tile {
        switch rotation {
        case .R90:
            return Tile(n: n, image: rotate90(image: image))
        case .R180:
            let tempImage = rotate90(image: image)
            return Tile(n: n, image: rotate90(image: tempImage))
        case .R270:
            return Tile(n: n, image: rotate270(image: image))
        }
    }


    private func flipped() -> Tile {
        Tile(n: n, image: flipped(image: image))
    }
}


extension Tile.Edge {
    var content: String {
        switch self {
        case .top(let c):
            return c
        case .right(let c):
            return c
        case .bottom(let c):
            return c
        case .left(let c):
            return c
        }
    }
}


// MARK: - Tile: Equatable

extension Tile: Equatable {
    static func == (lhs: Tile, rhs: Tile) -> Bool {
        lhs.n == rhs.n
    }
}


// MARK: - Edge: Equatable

extension Tile.Edge: Equatable {
    static func == (lhs: Tile.Edge, rhs: Tile.Edge) -> Bool {
        switch (lhs, rhs) {
        case (.top(let top1), .top(let top2)):
            return top1 == top2
        case (.right(let right1), .right(let right2)):
            return right1 == right2
        case (.bottom(let bottom1), .bottom(let bottom2)):
            return bottom1 == bottom2
        case (.left(let left1), .left(let left2)):
            return left1 == left2
        default:
            return false
        }
    }
}


// MARK: - CustomDebugStringConvertible

extension Tile: CustomDebugStringConvertible {
    var debugDescription: String {
        let content = image.joined(separator: "\n")
        return "Tile: \(self.n)\n----------\n\(content)\n"
    }
}


// MARK: - Private

private extension Tile {
    func rotate90(image: [String]) -> [String] {
        image.map({ Array($0) })
            .reversed()
            .transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
    }


    func rotate270(image: [String]) -> [String] {
        image.map({ Array( $0) })
            .transposed()
            .reversed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
    }


    func flipped(image: [String]) -> [String] {
        image.reversed()
    }
}
