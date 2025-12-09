package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Tile struct {
	x, y int
}

func Atoi(s string) int {
	number, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return number
}

func readInput(test bool) []Tile {
	fileName := "day09.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	lines := make([]Tile, 0)
	for l := range strings.Lines(string(data)) {
		splits := strings.Split(l[:len(l)-1], ",")
		lines = append(lines, Tile{x: Atoi(splits[0]), y: Atoi(splits[1])})
	}
	return lines
}

func area(t1, t2 Tile) int {
	dx := t1.x - t2.x
	dy := t1.y - t2.y
	if dx < 0 {
		dx = -dx
	}
	if dy < 0 {
		dy = -dy
	}
	dx++
	dy++
	return dx * dy
}

func part1(tiles []Tile) int {
	maxArea := 0
	for i, t1 := range tiles {
		for _, t2 := range tiles[i+1:] {
			a := area(t1, t2)
			if maxArea < a {
				maxArea = a
			}
		}
	}
	return maxArea
}

func isRectInside(t1, t2 Tile, tiles []Tile) bool {
	min_x := min(t1.x, t2.x)
	max_x := max(t1.x, t2.x)
	min_y := min(t1.y, t2.y)
	max_y := max(t1.y, t2.y)

	for i, t := range tiles {
		var prev Tile
		if i == 0 {
			prev = tiles[len(tiles)-1]
		} else {
			prev = tiles[i-1]
		}

		if prev.x == t.x {
			// vertical => check top and bottom
			if t.x <= min_x || t.x >= max_x {
				// skip on rect edge and beyond
				continue
			}
			if (min(prev.y, t.y) <= min_y && min_y < max(prev.y, t.y)) || (min(prev.y, t.y) < max_y && max_y <= max(prev.y, t.y)) || (min(prev.y, t.y) == min_y && max(prev.y, t.y) == max_y) {
				return false
			}
		} else {
			// horizontal => check left and right
			if t.y <= min_y || t.y >= max_y {
				// skip on rect edge and beyond
				continue
			}

			if (min(prev.x, t.x) <= min_x && min_x < max(prev.x, t.x)) || (min(prev.x, t.x) < max_x && max_x <= max(prev.x, t.x)) || (min(prev.x, t.x) == min_x && max(prev.x, t.x) == max_x) {
				return false
			}
		}

	}
	return true
}

func part2(tiles []Tile) int {
	maxArea := 0
	for i, t1 := range tiles {
		for _, t2 := range tiles[i+1:] {
			a := area(t1, t2)
			inside := isRectInside(t1, t2, tiles)
			if maxArea < a && inside {
				maxArea = a
			}
		}
	}
	return maxArea
}

func main() {
	// lines := readInput(true)
	lines := readInput(false)

	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}
