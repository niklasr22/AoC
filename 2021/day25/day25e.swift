import Darwin
import Cocoa

struct Key : Hashable {
    let x: Int
    let y: Int
    func hash(into hasher: inout Hasher) {
        hasher.combine(x)
        hasher.combine(y)
    }
}
func ==(lhs: Key, rhs: Key) -> Bool {
    return lhs.x == rhs.x && lhs.y == rhs.y
}

func loadInput() -> String {
    let path = "input.txt"
    do {
        return try String(contentsOfFile: path)
    } catch {
        return ""
    }
}

let input = loadInput()
let splittedInput = input.split(separator: "\n")

let height = splittedInput.count
let width =  splittedInput[0].count

var grid: [Key: Character] = [:]
for (y, row) in splittedInput.enumerated() {
    for (x, c) in row.enumerated() {
        if c != "." {
            grid[Key(x: x, y: y)] = c
        }
    }
}

func move() -> Bool {
    var moved = false
    var phase1: [Key: Character] = [:]
    var phase2: [Key: Character] = [:]

    for (coord,v) in grid {
        if v == ">" {
            let nX = (coord.x + 1) % width
            let nCoord = Key(x: nX, y: coord.y)
            if !grid.keys.contains(nCoord) {
                phase1[nCoord] = ">"
                moved = true
            } else {
                phase1[coord] = ">"
            }
        } else if v == "v" {
            phase1[coord] = "v"
        }
    }

    for (coord,v) in phase1 {
        if v == "v" {
            let nY = (coord.y + 1) % height
            let nCoord = Key(x: coord.x, y: nY)
            if !phase1.keys.contains(nCoord) {
                phase2[nCoord] = "v"
                moved = true
            } else {
                phase2[coord] = "v"
            }
        } else if v == ">" {
            phase2[coord] = ">"
        }
    }

    grid = phase2
    return moved
}

var i = 0
repeat {
    i += 1
} while move()

print(i)