//
//  Run12.swift
//  AdventOfCode2018
//
//  Created by gary on 22/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//
// 1300000000669
//

import Foundation

func run12() {
//    test12()
    main12()
}


func main12() {
    let data = Data12()
    let program = Program12(data: data)
    program.run(generations: 50_000_000_000)
}


func test12() {
    let data = Data12Test()
    let program = Program12(data: data)
    program.run(generations: 20)
}
