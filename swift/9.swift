
import Foundation

let PLAYER_COUNT = 459
let MARBLE_COUNT = 71790

/**
    Players
 */
final class Players {
    private let playerCount: Int
    private var playerScores: [Int: [Int]] = [:]
    
    init(playerCount: Int) {
        self.playerCount = playerCount
    }
    
    
    func getPlayerNo(fromMarbleNo marbleNo: Int) -> Int {
        let playerNo = marbleNo % playerCount
        if playerNo == 0 {
            return playerCount
        } else {
            return playerNo
        }
    }
    
    
    func add(marbleNo: Int) {
        let playerNo = getPlayerNo(fromMarbleNo: marbleNo)
        add(playerNo: playerNo, marbleNo: marbleNo)
    }
    
    
    func add(marbleNo: Int, otherMarbleNo: Int) {
        let playerNo = getPlayerNo(fromMarbleNo: marbleNo)
        add(playerNo: playerNo, marbleNo: otherMarbleNo)
    }
}



private extension Players {
    func add(playerNo: Int, marbleNo: Int) {
        if var scores = playerScores[playerNo] {
            scores.append(marbleNo)
            playerScores[playerNo] = scores
        } else {
            playerScores[playerNo] = [marbleNo]
        }
    }
}


extension Players: CustomDebugStringConvertible {
    var debugDescription: String {
        return playerScores.debugDescription
    }
}


/**
    The main game
 */
final class Game {
    private let specialNo = 23
    
    private let marbleCount: Int
    
    private var circle: [Int] = [0]
    private var currentMarble = 0
    private let players: Players
    
    init(playerCount: Int, marbleCount: Int) {
        self.marbleCount = marbleCount
        self.players = Players(playerCount: playerCount)
    }
    
    
    func run() {
        reset()
        for i in 1...marbleCount {
            if i % 23 == 0 {
                specialMove(i)
            } else {
                normalMove(i)
            }
        }
        print(players)
    }
}


private extension Game {
    var currentMarbleIndex: Int {
        return circle.firstIndex(of: currentMarble)!
    }
    
    
    func getNextIndex() -> Int {
        let indexCount = circle.indices.count
        let newIndex = (currentMarbleIndex + 2) % indexCount
        if newIndex == 0 {
            return indexCount
        } else {
            return newIndex
        }
    }
    
    
    func normalMove(_ marbleNo: Int) {
        let nextIndex = getNextIndex()
        circle.insert(marbleNo, at: nextIndex)
        currentMarble = marbleNo
    }
    
    
    func specialMove(_ marbleNo: Int) {
        players.add(marbleNo: marbleNo)
        let indexCount = circle.indices.count
        let indexToRemove = (currentMarbleIndex - 7) % indexCount
        let removedMarbleNo = circle.remove(at: indexToRemove)
        players.add(marbleNo: marbleNo, otherMarbleNo: removedMarbleNo)
        currentMarble = circle[indexToRemove]
    }
    
    
    func reset() {
        circle = [0]
        currentMarble = 0
    }
}


func main() {
    let game = Game(playerCount: PLAYER_COUNT, marbleCount: MARBLE_COUNT)
    game.run()
}


func test() {
    let game = Game(playerCount: 9, marbleCount: 25)
    game.run()
}


main()
test()
