package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type Box struct {
	x, y, z int
}

type Pair struct {
	i, j int
}

type DistPair struct {
	i, j, dist int
}

func Atoi(s string) int {
	number, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return number
}

func readInput(test bool) []Box {
	fileName := "day08.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	lines := make([]Box, 0)
	for l := range strings.Lines(string(data)) {
		splits := strings.Split(l[:len(l)-1], ",")
		lines = append(lines, Box{x: Atoi(splits[0]), y: Atoi(splits[1]), z: Atoi(splits[2])})
	}
	return lines
}

func dist(b1, b2 Box) int {
	return (b1.x-b2.x)*(b1.x-b2.x) + (b1.y-b2.y)*(b1.y-b2.y) + (b1.z-b2.z)*(b1.z-b2.z)
}

func closestPairs(boxes []Box) []DistPair {
	dists := make([]DistPair, 0, len(boxes)*len(boxes))
	for i, b1 := range boxes {
		for j, b2 := range boxes[i+1:] {
			d := dist(b1, b2)
			dists = append(dists, DistPair{i: i, j: i + j + 1, dist: d})
		}
	}
	slices.SortFunc(dists, func(a, b DistPair) int {
		if a.dist == b.dist {
			return 0
		} else if a.dist < b.dist {
			return -1
		}
		return 1
	})
	return dists
}

func part1(boxes []Box, limit int) int {
	circuits := make(map[int]int, 0)
	circuitId := 0

	dists := closestPairs(boxes)

	for _, pair := range dists[:limit] {
		b1 := pair.i
		b2 := pair.j

		cb1, b1AlreadyInCurcuit := circuits[b1]
		cb2, b2AlreadyInCurcuit := circuits[b2]

		if b1AlreadyInCurcuit && b2AlreadyInCurcuit {
			if cb1 == cb2 {
				continue
			}

			for b, c := range circuits {
				if c == cb2 {
					circuits[b] = cb1
				}
			}
		} else if !b1AlreadyInCurcuit && !b2AlreadyInCurcuit {
			circuits[b1] = circuitId
			cb1 = circuitId
			circuitId++
			circuits[b2] = cb1
		} else if b1AlreadyInCurcuit {
			circuits[b2] = cb1
		} else if b2AlreadyInCurcuit {
			circuits[b1] = cb2
		}
	}

	sizes := make(map[int]int, 0)
	for _, c := range circuits {
		sizes[c]++
	}

	sizesList := make([]int, 0, len(sizes))
	for _, s := range sizes {
		sizesList = append(sizesList, s)
	}

	slices.Sort(sizesList)
	result := 1
	for _, s := range sizesList[len(sizesList)-3:] {
		result *= s
	}

	return result
}

func part2(boxes []Box) int {
	circuits := make(map[int]int, 0)
	circuitId := 0
	dists := closestPairs(boxes)
	var lastPair Pair
	circuitCount := 0
	for i, pair := range dists {
		b1 := pair.i
		b2 := pair.j
		lastPair = Pair{i: b1, j: b2}

		cb1, b1AlreadyInCurcuit := circuits[b1]
		cb2, b2AlreadyInCurcuit := circuits[b2]

		if b1AlreadyInCurcuit && b2AlreadyInCurcuit {
			if cb1 == cb2 {
				continue
			}

			for b, c := range circuits {
				if c == cb2 {
					circuits[b] = cb1
				}
			}
			circuitCount--
		} else if !b1AlreadyInCurcuit && !b2AlreadyInCurcuit {
			circuits[b1] = circuitId
			cb1 = circuitId
			circuitId++
			circuits[b2] = cb1
			circuitCount++
		} else if b1AlreadyInCurcuit {
			circuits[b2] = cb1
		} else if b2AlreadyInCurcuit {
			circuits[b1] = cb2
		}

		// heuristic
		if circuitCount == 1 && i > 100 {
			break
		}
	}
	sizes := make(map[int]int, 0)
	for _, c := range circuits {
		sizes[c]++
	}

	result := boxes[lastPair.i].x * boxes[lastPair.j].x

	return result
}

func main() {
	// boxes := readInput(true)
	// limit := 10

	boxes := readInput(false)
	limit := 1000

	fmt.Println("Part 1:", part1(boxes, limit))
	fmt.Println("Part 2:", part2(boxes))
}
