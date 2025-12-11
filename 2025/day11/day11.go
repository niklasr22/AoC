package main

import (
	"fmt"
	"os"
	"strings"
)

func readInput(test bool) map[string][]string {
	fileName := "day11.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	nodes := make(map[string][]string, 0)
	for l := range strings.Lines(string(data)) {
		labelSplit := strings.Split(l, ":")
		label := labelSplit[0]
		next := strings.Split(strings.TrimSpace(labelSplit[1]), " ")
		nodes[label] = next
	}
	return nodes
}

func bfs(graph map[string][]string, current string) int {
	if current == "out" {
		return 1
	}
	count := 0
	for _, next := range graph[current] {
		count += bfs(graph, next)
	}
	return count
}

type Key struct {
	current  string
	fft, dac bool
}

var p2_memo = make(map[Key]int)

func bfs_p2(graph map[string][]string, current string, fft, dac bool) int {
	k := Key{
		current: current,
		fft:     fft,
		dac:     dac,
	}
	mem, ok := p2_memo[k]
	if ok {
		return mem
	}

	if current == "out" {
		if fft && dac {
			return 1
		}
		return 0
	}
	count := 0
	for _, next := range graph[current] {
		count += bfs_p2(graph, next, fft || current == "fft", dac || current == "dac")
	}
	p2_memo[k] = count
	return count
}

func part1(graph map[string][]string) int {
	return bfs(graph, "you")
}

func part2(graph map[string][]string) int {
	return bfs_p2(graph, "svr", false, false)
}

func main() {
	graph := readInput(false)

	fmt.Println("Part 1:", part1(graph))
	fmt.Println("Part 2:", part2(graph))
}
