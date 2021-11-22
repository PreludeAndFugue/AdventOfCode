//
//  Collection+Extension.swift
//  AdventOfCode2020
//
//  Created by gary on 12/12/2020.
//

import Foundation

extension Collection where Element: AdditiveArithmetic {
    func sum() -> Element {
        reduce(.zero, +)
    }
}


extension Collection where Element: Numeric {
    func product() -> Element {
        reduce(1, *)
    }
}


extension Collection where Self.Iterator.Element: RandomAccessCollection {
    func transposed() -> [[Self.Iterator.Element.Iterator.Element]] {
        guard let firstRow = self.first else { return [] }
        return firstRow.indices.map() { index in
            self.map({ $0[index] })
        }
    }
}
