//
//  Day06.swift
//  AdventOfCode2022
//
//  Created by gary on 06/12/2022.
//

import Foundation

fileprivate let test0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
fileprivate let test1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
fileprivate let test2 = "nppdvjthqldpwncqszvftbrmjlhg"
fileprivate let test3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
fileprivate let test4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

struct Day06: Day {
    let d = "06"

    func run() throws -> (String, String) {
        let s = try getInput()

        testPart1()
        let p1 = part(s: s, n: 4)
        testPart2()
        let p2 = part(s: s, n: 14)

        return ("\(p1)", "\(p2)")
    }
}


// MARK: - Private

private extension Day06 {
    func part(s: String, n: Int) -> Int {
        let l = s.count
        for i in 0..<(l - n) {
            let i1 = s.index(s.startIndex, offsetBy: i)
            let i2 = s.index(s.startIndex, offsetBy: i + n - 1)
            let p = s[i1...i2]
            let items = Set(p)
            if items.count == n {
                return i + n
            }
        }
        fatalError()
    }


    func testPart1() {
        assert(part(s: test0, n: 4) == 7)
        assert(part(s: test1, n: 4) == 5)
        assert(part(s: test2, n: 4) == 6)
        assert(part(s: test3, n: 4) == 10)
        assert(part(s: test4, n: 4) == 11)
    }


    func testPart2() {
        assert(part(s: test0, n: 14) == 19)
        assert(part(s: test1, n: 14) == 23)
        assert(part(s: test2, n: 14) == 23)
        assert(part(s: test3, n: 14) == 29)
        assert(part(s: test4, n: 14) == 26)
    }
}
