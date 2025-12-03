package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput(test bool) []string {
	filePath := "./inputs/day03.txt"
	if test {
		filePath = "./test/day03.txt"
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

func findMax(s string) (rune, int) {
	maxBat := rune(s[0])
	maxBatInd := 0
	for i, c := range s[1:] {
		if maxBat < c {
			maxBat = c
			maxBatInd = i + 1
		}
	}
	return maxBat, maxBatInd
}

func part1(batteries []string) {
	joltage := 0
	for _, bank := range batteries {
		first, firstInd := findMax(bank[:len(bank)-1])
		second, _ := findMax(bank[firstInd+1:])

		packJoltage, err := strconv.Atoi(string(first) + string(second))
		if err != nil {
			panic(err)
		}
		joltage += packJoltage
	}

	fmt.Println("Part 1 Joltage:", joltage)
}

func part2(batteries []string) {
	joltage := 0
	targetAmt := 12
	for _, bank := range batteries {
		selection := ""

		start := 0
		for i := 0; i < targetAmt; i++ {
			val, ind := findMax(bank[start : len(bank)-targetAmt+len(selection)+1])
			selection += string(val)
			start += 1 + ind
		}

		packJoltage, err := strconv.Atoi(selection)
		if err != nil {
			panic(err)
		}
		joltage += packJoltage
	}

	fmt.Println("Part 2 Joltage:", joltage)

}

func main() {
	// inputs := parseInput(true)
	inputs := parseInput(false)
	part1(inputs)
	part2(inputs)
}
