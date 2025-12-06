package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Atoi(s string) uint64 {
	number, err := strconv.ParseUint(s, 10, 64)
	if err != nil {
		panic(err)
	}
	return number
}

func readInput(test bool) []string {
	fileName := "day06.txt"
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

func parseInputPart1(test bool) ([][]int, []rune) {
	lines := readInput(test)
	problems := make([][]int, 0)
	ops := make([]rune, 0)

	last := -1
	for i, c := range lines[len(lines)-1] {
		if c == ' ' && i != len(lines[0])-1 {
			continue
		}
		if last == -1 {
			last = i
			continue
		}
		if i == len(lines[0])-1 {
			i++
		}
		ops = append(ops, ([]rune(lines[len(lines)-1]))[last])
		problem := make([]int, 0)
		for _, row := range lines[:len(lines)-1] {
			problem = append(problem, int(Atoi(strings.TrimSpace(row[last:i]))))
		}
		problems = append(problems, problem)
		last = i
	}

	return problems, ops
}

func parseInputPart2(test bool) ([][]int, []rune) {
	lines := readInput(test)
	problems := make([][]int, 0)
	ops := make([]rune, 0)

	var problem []int = nil
	for i, c := range lines[len(lines)-1] {
		if c != ' ' {
			if problem != nil {
				problems = append(problems, problem)
			}
			problem = make([]int, 0)
			ops = append(ops, c)
		}

		number := make([]rune, len(lines)-1)
		for l, row := range lines[:len(lines)-1] {
			number[l] = rune(row[i])
		}
		numberStr := strings.TrimSpace(string(number))
		if numberStr == "" {
			continue
		}
		problem = append(problem, int(Atoi(numberStr)))
	}
	problems = append(problems, problem)

	return problems, ops
}

func mul(a, b int) int {
	return a * b
}

func sum(a, b int) int {
	return a + b
}

func evaluate(problems [][]int, ops []rune) int {
	total := 0
	for i, problem := range problems {
		operation := sum
		result := 0
		if ops[i] == '*' {
			operation = mul
			result = 1
		}
		for _, c := range problem {
			result = operation(result, c)
		}
		total += result
	}
	return total
}

func main() {
	problems, ops := parseInputPart1(false)
	fmt.Println("Part 1:", evaluate(problems, ops))

	problems, ops = parseInputPart2(false)
	fmt.Println("Part 2:", evaluate(problems, ops))
}
