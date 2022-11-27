//
//  CGRect+Extensions.swift
//  AdventOfCode2018
//
//  Created by gary on 21/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

extension CGRect {
    var width: CGFloat {
        return self.size.width
    }
    var height: CGFloat {
        size.height
    }
    var minX: CGFloat {
        let x1 = self.origin.x
        let x2 = self.origin.x + self.size.width
        return min(x1, x2)
    }
    var minY: CGFloat {
        let y1 = self.origin.y
        let y2 = origin.y + size.height
        return min(y1, y2)
    }
    var area: CGFloat {
        return width * height
    }
}
