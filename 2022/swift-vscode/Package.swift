// swift-tools-version:5.7.1
import PackageDescription

let package = Package(
    name: "AdventOfCode2022",
    platforms: [
        .macOS(.v12),
    ],
    products: [
        .executable(name: "AdventOfCode2022", targets: ["AdventOfCode2022"])
        // .library(name: "AdventOfCode2022", targets: ["AdventOfCode2022"])
    ],
    dependencies: [
        // .package(url: "https://url/of/another/package/named/utility", from: "1.0.0")
    ],
    targets: [
        .executableTarget(name: "AdventOfCode2022", dependencies: []),
        .testTarget(name: "AdventOfCode2022Tests", dependencies: ["AdventOfCode2022"])
    ]
)
