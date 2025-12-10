package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Machine struct {
	indicators int
	btns       []int
	btnIndices [][]int
	joltages   []int
}

func Atoi(s string) int {
	number, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return number
}

func readInput(test bool) []Machine {
	fileName := "day10.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	machines := make([]Machine, 0)
	for l := range strings.Lines(string(data)) {
		indicatorFinder := regexp.MustCompile(`\[([.#]+)\]`)
		indicatorStr := indicatorFinder.FindString(l)
		indicators := 0
		for i, r := range strings.Trim(indicatorStr, "[]") {
			if r == '#' {
				indicators |= 1 << i
			}
		}

		joltageFinder := regexp.MustCompile(`\{([0-9,]+)\}`)
		joltageStr := joltageFinder.FindString(l)
		joltageStrs := strings.Split(strings.Trim(joltageStr, "{}"), ",")
		joltages := make([]int, 0, len(joltageStrs))
		for _, j := range joltageStrs {
			joltages = append(joltages, Atoi(j))
		}

		buttonFinder := regexp.MustCompile(`\(([0-9,]+)\)`)
		buttonStrs := buttonFinder.FindAllString(l, -1)
		buttons := make([]int, 0, len(buttonStrs))
		for _, b := range buttonStrs {
			btn := 0
			for _, x := range strings.Split(strings.Trim(b, "()"), ",") {
				num := Atoi(x)
				btn |= 1 << num
			}
			buttons = append(buttons, btn)
		}

		machines = append(machines, Machine{indicators: indicators, btns: buttons, joltages: joltages})
	}
	return machines
}

func part1(machines []Machine) int {
	result := 0
	for _, m := range machines {
		mem := make([]int, 0)
		mem = append(mem, 0) // initial indicators
		presses := 0
		found := false
		for !found {
			newMem := make([]int, 0, len(mem)*len(m.btns))
			for _, state := range mem {
				for _, btn := range m.btns {
					newState := state ^ btn
					if newState == m.indicators {
						found = true
						break
					}
					newMem = append(newMem, newState)
				}
				if found {
					break
				}
			}
			mem = newMem
			presses++
		}
		result += presses
	}

	return result
}

func main() {
	// machines := readInput(true)
	machines := readInput(false)

	fmt.Println("Part 1:", part1(machines))
}
