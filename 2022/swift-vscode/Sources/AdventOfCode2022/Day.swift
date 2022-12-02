import Foundation

protocol Day {
    var d: String { get }
    func run() throws -> (String, String)
}


extension Day {
    func getInput() throws -> String {
        let fm = FileManager()
        let url = fm.homeDirectoryForCurrentUser.appendingPathComponent("Documents")
            .appendingPathComponent("computing")
            .appendingPathComponent("_AdventOfCode")
            .appendingPathComponent("2022")
            .appendingPathComponent("day\(d).txt")
        return try String(contentsOf: url, encoding: .utf8)
    }
}