//
//  Run10.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

func run10() {
    let pointParser = PointParser()
    let points = pointParser.parseAll(string: DATA_10)
    for i in 1..<39985 {
        points.forEach({ $0.move() })
        let boundingBox = getBoundingBox(points: points)
        if boundingBox.area < 10_000 {
            print()
            print(i)
            print(points: points)
            print()
        }
    }
}


private func getBoundingBox(points: [Point]) -> CGRect {
    let xValues = points.map({ $0.x })
    let yValues = points.map({ $0.y })
    let minX = xValues.min()!
    let maxX = xValues.max()!
    let minY = yValues.min()!
    let maxY = yValues.max()!
    return CGRect(
        origin: CGPoint(x: Double(minX), y: Double(minY)),
        size: CGSize(width: Double(maxX) - Double(minX), height: Double(maxY) - Double(minY))
    )
//    return CGRect(x: minX, y: minY, width: maxX - minX, height: maxY - minY)
}


private func print(points: [Point]) {
    let boundingBox = getBoundingBox(points: points)
    let minX = Int(boundingBox.minX)
    let minY = Int(boundingBox.minY)
    let width = Int(boundingBox.width)
    let height = Int(boundingBox.height)
    var picture = Array(repeating: Array(repeating: ".", count: width + 1), count: height + 1)
    for point in points {
        picture[point.y - minY][point.x - minX ] = "#"
    }
    print(picture.map({ $0.joined() }).joined(separator: "\n"))
}
