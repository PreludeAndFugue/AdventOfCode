//
//  Image.swift
//  AdventOfCode2020
//
//  Created by gary on 22/12/2020.
//

import Foundation

final class Image {
    enum Rotation {
        case R90
        case R180
        case R270
    }


    let content: [String]

    init(content: [String]) {
        self.content = content
    }


    func rotated(_ rotation: Rotation) -> Image {
        switch rotation {
        case .R90:
            return Image(content: rotate90(content: content))
        case .R180:
            let tempContent = rotate90(content: content)
            return Image(content: rotate90(content: tempContent))
        case .R270:
            return Image(content: rotate270(content: content))
        }
    }


    func flipped() -> Image {
        Image(content: content.reversed())
    }
}


// MARK: - Private

private extension Image {
    func rotate90(content: [String]) -> [String] {
        content.map({ Array($0) })
            .reversed()
            .transposed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
    }


    func rotate270(content: [String]) -> [String] {
        content.map({ Array( $0) })
            .transposed()
            .reversed()
            .map({ $0.map({ String($0) }).joined(separator: "") })
    }
}
