import Foundation


func read(_ fileName: String) -> String {
    let url = Bundle.main.url(forResource: fileName, withExtension: "txt")!
    return try! String(contentsOf: url)
}


func parseInts(_ string: String) -> [Int] {
    string.trimmingCharacters(in: .whitespacesAndNewlines)
        .split(separator: ",")
        .map({ Int($0)! })
}
