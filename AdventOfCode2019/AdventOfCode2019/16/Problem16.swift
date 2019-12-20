//
//  Problem16.swift
//  AdventOfCode2019
//
//  Created by gary on 19/12/2019.
//  Copyright © 2019 Gary Kerr. All rights reserved.
//

final class Problem16: Problem {
    func run() {
        let r1 = part1()
        let r2 = 0
        printResults(number: 16, r1, r2)
    }
}


// MARK: - Private

private extension Problem16 {
    private func part1() -> Int {
        var signal = makeInput(string: input7)
        signal = signal + signal + signal + signal + signal + signal + signal + signal + signal + signal + signal + signal + signal + signal + signal
        for position in 0...100 {
            print(position, makeOutput(a: signal))
            signal = fft(a: signal, position: position)
        }


        return 0
    }


    private func makePattern(position: Int, length: Int) -> [Int] {
        if let pattern = patterns[position] {
            return pattern
        }
        var result: [Int] = []
        var i = 0
        while true {
            for n in basePattern {
                for _ in 0..<position {
                    result.append(n)
                    if i == length {
                        let answer = Array(result[1...])
                        patterns[position] = answer
                        return answer
                    }
                    i += 1
                }
            }
        }
    }


    private func makeInput(string: String) -> [Int] {
        var result: [Int] = []
        for ch in string {
            result.append(Int(String(ch))!)
        }
        return result
    }


    private func multiply(a: [Int], b: [Int]) -> [Int] {
        zip(a, b).map({ $0 * $1 })
    }


    private func normalise(a: Int) -> Int {
        let b = a % 10
//        print(a, b)
        if b < 0 {
            return abs(b)
        } else {
            return b
        }
    }


    private func fft(a: [Int], position: Int) -> [Int] {
        let length = a.count
        var result = Array(repeating: 0, count: length)
        for position in 1...a.count {
            let pattern = makePattern(position: position, length: length)
//            print(a, pattern)
            let n = normalise(a: multiply(a: a, b: pattern).sum())
            result[position - 1] = n
        }
        return result
    }


    private func makeOutput(a: [Int]) -> String {
//        a[..<8].map({ String($0) }).joined()
        a.map({ String($0) }).joined()
    }
}

private let basePattern = [0, 1, 0, -1]
/// A cache of the patterns
private var patterns: [Int: [Int]] = [:]


private let input = "59728776137831964407973962002190906766322659303479564518502254685706025795824872901465838782474078135479504351754597318603898249365886373257507600323820091333924823533976723324070520961217627430323336204524247721593859226704485849491418129908885940064664115882392043975997862502832791753443475733972832341211432322108298512512553114533929906718683734211778737511609226184538973092804715035096933160826733751936056316586618837326144846607181591957802127283758478256860673616576061374687104534470102346796536051507583471850382678959394486801952841777641763547422116981527264877636892414006855332078225310912793451227305425976335026620670455240087933409"


private let input2 = "12345678"

private let input3 = "80871224585914546619083218645595"

private let input4  = "19617804207202209144916044189917"

private let input5 = "69317163492948606335995924319873"

private let input6 = "03036732577212944063491565474664"

private let input7 = "02935109699940807407585447034323"
