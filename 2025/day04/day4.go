package main

import (
	"fmt"
	"os"
	"strings"
)

func parseInput(test bool) []string {
	filePath := "./inputs/day04.txt"
	if test {
		filePath = "./test/day04.txt"
	}
	data, err := os.ReadFile(filePath)
	if err != nil {
		panic(err)
	}

	lines := make([]string, 0)
	for l := range strings.Lines(string(data)) {
		lines = append(lines, l[:len(l)-1])
	}
	return lines
}

func adjacents(grid [][]rune, x, y int) int {
	adjacents := 0

	for i := max(0, y-1); i < min(y+2, len(grid)); i++ {
		for j := max(0, x-1); j < min(x+2, len(grid[i])); j++ {
			if i == y && j == x {
				continue
			}
			if grid[i][j] == '@' {
				adjacents++
			}
		}
	}

	return adjacents
}

func part1(grid [][]rune) {
	count := 0
	for y, row := range grid {
		for x, place := range row {
			if place == '.' {
				continue
			}
			if adjacents(grid, x, y) < 4 {
				count++
			}
		}
	}
	fmt.Println("Part 1:", count)
}

func part2(grid [][]rune) {
	check := true
	removals := 0

	type coord struct{ x, y int }

	for check {
		count := 0
		to_be_removed := make([]coord, 0)
		for y, row := range grid {
			for x, place := range row {
				if place == '.' {
					continue
				}
				if adjacents(grid, x, y) < 4 {
					count++
					to_be_removed = append(to_be_removed, coord{
						x: x,
						y: y,
					})
				}
			}
		}
		for _, tbr := range to_be_removed {
			grid[tbr.y][tbr.x] = '.'
		}
		removals += count
		check = count > 0
	}
	fmt.Println("Part 2:", removals)
}

func main() {
	// gridInput := parseInput(true)
	gridInput := parseInput(false)

	grid := make([][]rune, len(gridInput))
	for y, row := range gridInput {
		grid[y] = []rune(row)
	}
	part1(grid)
	part2(grid)
}
