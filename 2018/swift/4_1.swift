/**
    Problem 4
    
    Sample data
    
    [1518-04-06 00:00] Guard #499 begins shift
    [1518-04-06 00:09] falls asleep
    [1518-04-06 00:32] wakes up
    [1518-04-06 00:43] falls asleep
    [1518-04-06 00:55] wakes up
    [1518-04-06 23:59] Guard #1783 begins shift
    [1518-04-07 00:08] falls asleep
    [1518-04-07 00:55] wakes up
*/

import Foundation

let INPUT = "4.txt"

typealias SleepMinutes = [Int: [Int]]

let timeRegex = try! NSRegularExpression(pattern: "\\[\\d+-\\d+-\\d+ \\d+:(\\d+)")
let idRegex = try! NSRegularExpression(pattern: "#(\\d+)")


// Extensions

extension NSRegularExpression {
    func firstMatch(in string: String) -> NSTextCheckingResult? {
        let range = NSRange(location: 0, length: string.utf16.count)
        return firstMatch(in: string, options: [], range: range)
    }
}


enum Item {
    case start(Int)
    case fallAsleep(Int)
    case wakeUp(Int)
}


struct GuardSleep {
    let id: Int
    let start: Int
    let end: Int
    
    var minutes: [Int] {
        return Array(start..<end)
    }
}


func getInput() -> [Item] {
    enum State {
        case awake
        case asleep
        
        func makeItem(_ time: Int) -> Item {
            switch self {
                case .awake: return .fallAsleep(time)
                case .asleep: return .wakeUp(time)
            }
        }
        
        mutating func toggle() {
            switch self {
                case .awake: self = .asleep
                case .asleep: self = .awake
            }
        }
    }
    
    func getId(_ string: String) -> Int? {
        guard
            let match = idRegex.firstMatch(in: string),
            let idRange = Range(match.range(at: 1), in: string)
        else {
            return nil
        }
        return Int(string[idRange])
    }
    
    func getTime(_ string: String) -> Int? {
        guard 
            let match = timeRegex.firstMatch(in: string),
            let timeRange = Range(match.range(at: 1), in: string)
        else {
            return nil
        }
        return Int(string[timeRange])
    }
    
    let string = try! String(contentsOfFile: INPUT)
    var items: [Item] = []
    var state = State.awake
    for line in string.split(separator: "\n").sorted().map({ String($0) }) {
        if let id = getId(line) {
            items.append(.start(id))
        } else if let time = getTime(line) {
            items.append(state.makeItem(time))
            state.toggle()
        } else {
            fatalError("couldn't parse line: \(line)")
        }
    }
    return items
}


func makeSleeps(from items: [Item]) -> [GuardSleep] {
    var currentId: Int = 0
    var currentStart: Int = 0
    var results: [GuardSleep] = []
    for item in items {
        switch item {
            case .start(let id):
                currentId = id
            case .fallAsleep(let time):
                currentStart = time
            case .wakeUp(let time):
                let sleep = GuardSleep(id: currentId, start: currentStart, end: time)
                results.append(sleep)
        }
    }
    return results
}


func makeSleepMinutes(from sleeps: [GuardSleep]) -> SleepMinutes {
    var result: SleepMinutes = [:]
    for sleep in sleeps {
        if var minutes = result[sleep.id] {
            minutes.append(contentsOf: sleep.minutes)
            result[sleep.id] = minutes
        } else {
            result[sleep.id] = sleep.minutes
        }
    }
    return result
}


func findBestSleeper(from sleepMinutes: SleepMinutes) -> (id: Int, minutes: [Int]) {
    let best = sleepMinutes.map({ ($1.count, $0, $1) }).sorted(by: { $0.0 > $1.0 }).first!
    return (id: best.1, minutes: best.2)
}


func findMostSleptMinute(_ minutes: [Int]) -> (minute: Int, count: Int) {
    var counter: [Int: Int] = [:]
    for minute in minutes {
        if let value = counter[minute] {
            counter[minute] = value + 1
        } else {
            counter[minute] = 1
        }
    }
    let best = counter.sorted(by: {$0.value > $1.value }).first!
    return (minute: best.key, count: best.value)
}


func main() {
    let items = getInput()
    let sleeps = makeSleeps(from: items)
    let sleepMinutes = makeSleepMinutes(from: sleeps)
    
    let (id, minutes) = findBestSleeper(from: sleepMinutes)
    let (mostSleptMinute, _) = findMostSleptMinute(minutes)
    print(id, mostSleptMinute, id * mostSleptMinute)
    
    let bestSleepMinutes = sleepMinutes.mapValues({ findMostSleptMinute($0) })
    let best = bestSleepMinutes.sorted(by: { $0.value.count > $1.value.count }).first!
    print(best.key * best.value.minute)
}


main()