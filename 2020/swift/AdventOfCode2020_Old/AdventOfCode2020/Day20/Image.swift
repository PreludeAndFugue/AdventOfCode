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

    init(image: [String]) {
        self.content = image
    }


    func rotated(_ rotation: Rotation) -> Image {
        Image(image: content.reversed())
    }
}


// MARK: - Private

private extension Image {

}
