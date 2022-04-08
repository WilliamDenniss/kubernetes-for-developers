// swift-tools-version:4.2

import PackageDescription

let package = Package(
    name: "ContainerizedSwift",
    dependencies: [
    ],
    targets: [
        .target(
            name: "ContainerizedSwift",
            dependencies: [],
            path: ".",
            sources: ["Source"]
        )
    ]
)
