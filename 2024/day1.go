package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("2024/inputs/day1.txt")

	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(data), "\n")

	list1 := make([]int, len(lines))
	list2 := make([]int, len(lines))

	for i, line := range lines {
		numbers := strings.Split(line, " ")
		list1[i], err = strconv.Atoi(numbers[0])
		if err != nil {
			panic(err)
		}
		list2[i], err = strconv.Atoi(numbers[len(numbers)-1])
		if err != nil {
			panic(err)
		}
	}

	sort.Ints(list1)
	sort.Ints(list2)

	dist := 0
	for i := range list1 {
		d := list2[i] - list1[i]
		if d < 0 {
			d = -d
		}
		dist += d
	}
	fmt.Println("a:", dist)

	score := 0
	for i := range list1 {
		occurences := 0
		for j := range list2 {
			if list1[i] == list2[j] {
				occurences++
			}
		}
		score += list1[i] * occurences
	}

	fmt.Println("b:", score)

}
