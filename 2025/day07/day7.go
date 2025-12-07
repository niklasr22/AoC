package main

import (
	"fmt"
	"os"
	"strings"
)

func readInput(test bool) []string {
	fileName := "day07.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	lines := make([]string, 0)
	for l := range strings.Lines(string(data)) {
		lines = append(lines, l[:len(l)-1])
	}
	return lines
}

func part1(lines []string) int {
	beams := make(map[int]struct{})

	beams[strings.Index(lines[0], "S")] = struct{}{}

	splits := 0
	for i := 1; i < len(lines); i++ {
		newBeams := make(map[int]struct{})
		for beam := range beams {
			if lines[i][beam] == byte('^') {
				newBeams[beam-1] = struct{}{}
				newBeams[beam+1] = struct{}{}
				splits++
			} else {
				newBeams[beam] = struct{}{}
			}
		}
		beams = newBeams
	}

	return splits
}

func part2(lines []string) int {
	beams := make(map[int]int)

	beams[strings.Index(lines[0], "S")] = 1

	splits := 0
	for i := 1; i < len(lines); i++ {
		newBeams := make(map[int]int)
		for beam, beamCount := range beams {
			if lines[i][beam] == byte('^') {
				newBeams[beam-1] += beamCount
				newBeams[beam+1] += beamCount
				splits++
			} else {
				newBeams[beam] += beamCount
			}
		}
		beams = newBeams
	}

	timelines := 0
	for _, count := range beams {
		timelines += count
	}

	return timelines
}

func main() {
	// lines := readInput(true)
	lines := readInput(false)

	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}
