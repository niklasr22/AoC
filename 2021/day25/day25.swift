import Darwin
import Cocoa

func loadInput() -> String {
    let path = "input.txt"
    do {
        return try String(contentsOfFile: path)
    } catch {
        return ""
    }
}

let input = loadInput()
var grid = input.split(separator: "\n").map { (line) -> [Character] in return Array(line) }

func printGrid(g: [[Character]]) {
    for r in g {
        print(String(r))
    }
    print("-------------------\n")
}

func move() -> Bool {
    let height = grid.count
    let width =  grid[0].count
    var moved = false
    var phase1: [[Character]] = []
    var phase2: [[Character]] = []
    for _ in 0..<height {
        var row1: [Character] = []
        var row2: [Character] = []
        for _ in 0..<width {
            row1.append(".")
            row2.append(".")
        }
        phase1.append(row1)
        phase2.append(row2)
    }
    for y in 0..<height {
        for x in 0..<width {
            let nX = (x + 1) % width
            if grid[y][x] == ">" && grid[y][nX] == "." {
                phase1[y][nX] = ">"
                moved = true
            } else if grid[y][x] != "." {
                phase1[y][x] = grid[y][x]
            }
        }
    }
    //printGrid(g: phase1)
    for y in 0..<height {
        let nY = (y + 1) % height
        for x in 0..<width {
            if phase1[y][x] == "v" && phase1[nY][x] == "." {
                phase2[nY][x] = "v"
                moved = true
            } else if phase1[y][x] != "." {
                phase2[y][x] = phase1[y][x]
            }
        }
    }
    //printGrid(g: phase2)
    grid = phase2
    return moved
}

var i = 0
repeat {
    i += 1
} while move()

print(i)