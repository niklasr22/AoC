package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type freshRange struct {
	low, high uint64
}

func Atoi(s string) uint64 {
	number, err := strconv.ParseUint(s, 10, 64)
	if err != nil {
		panic(err)
	}
	return number
}

func parseInput(test bool) ([]freshRange, []uint64) {
	fileName := "day05.txt"
	filePath := "./inputs/"
	if test {
		filePath = "./test/"
	}
	data, err := os.ReadFile(filePath + fileName)
	if err != nil {
		panic(err)
	}

	ranges := make([]freshRange, 0)
	ids := make([]uint64, 0)
	isRange := true
	for l := range strings.Lines(string(data)) {
		if len(l) <= 1 {
			isRange = false
			continue
		}
		if isRange {
			splits := strings.Split(l[:len(l)-1], "-")
			fr := freshRange{
				low:  Atoi(splits[0]),
				high: Atoi(splits[1]),
			}

			ranges = append(ranges, fr)
		} else {
			number := Atoi(l[:len(l)-1])
			ids = append(ids, number)
		}
	}
	return ranges, ids
}

func part1(ranges []freshRange, ids []uint64) int {
	freshCount := 0
	for _, id := range ids {
		for _, r := range ranges {
			if r.low <= id && id <= r.high {
				freshCount++
				break
			}
		}
	}
	return freshCount
}

func part2(ranges []freshRange) uint64 {
	cleanedRanges := make([]freshRange, 0)
	cleanedRanges = append(cleanedRanges, ranges[0])
	ranges = ranges[1:]
	for len(ranges) > 0 {
		r := ranges[0]
		ranges = ranges[1:]
		invalidated := -1
		contained := false
		for i, c := range cleanedRanges {
			if c.low <= r.low && r.high <= c.high {
				contained = true
				break
			}
			if r.low <= c.low && c.high <= r.high {
				cleanedRanges[i].low = r.low
				cleanedRanges[i].high = r.high
				invalidated = i + 1
				break
			}
			if c.low <= r.low && r.low <= c.high && c.high < r.high {
				cleanedRanges[i].high = r.high
				invalidated = i + 1
				break
			}
			if r.low < c.low && c.low <= r.high && r.high <= c.high {
				cleanedRanges[i].low = r.low
				invalidated = i + 1
				break
			}
		}
		if contained {
			continue
		}
		if invalidated != -1 {
			ranges = append(ranges, cleanedRanges[invalidated:]...)
			cleanedRanges = cleanedRanges[:invalidated]
		} else {
			cleanedRanges = append(cleanedRanges, r)
		}
	}
	var freshCount uint64 = 0
	for _, c := range cleanedRanges {
		freshCount += c.high - c.low + 1
	}
	return freshCount
}

func main() {
	// ranges, ids := parseInput(true)
	ranges, ids := parseInput(false)

	fmt.Println("Part 1:", part1(ranges, ids))
	fmt.Println("Part 2:", part2(ranges))
}
