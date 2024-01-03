//
//  main.swift
//  AdventOfCode2023_CmdLine
//
//  Created by gary on 03/01/2024.
//

import Foundation


func getInput(_ day: String) -> String {
    let fm = FileManager.default
    let filePath = fm.homeDirectoryForCurrentUser
        .appending(path: "Documents")
        .appending(path: "computing")
        .appending(path: "_AdventOfCode")
        .appending(path: "2023")
        .appending(path: "day\(day).txt")
    return try! String(contentsOf: filePath)
}

Day01().run()
