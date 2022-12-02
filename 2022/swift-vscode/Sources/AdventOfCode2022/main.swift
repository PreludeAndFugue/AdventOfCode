

let d = Day01()

do {
    let (p1, p2) = try d.run()
    print("Part1:", p1)
    print("Part2:", p2)
} catch let error {
    print(error)
}