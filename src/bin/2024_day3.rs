use core::str;
use std::{fs};
use regex::Regex;

fn part1(instructions: &str) -> i32 {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let mut result = 0;

    for (_, [a, b]) in re.captures_iter(instructions).map(|c| c.extract()) {
        result += a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap();
    }
    return result;
}


fn part2(instructions: &str) -> i32 {
    let re = Regex::new(r"mul\((\d+,\d+)\)|(do\(\))|(don't\(\))").unwrap();

    let mut result = 0;

    let mut enabled = true;
    for (_, [capture]) in re.captures_iter(instructions).map(|c| c.extract()) {
        if capture == "do()" {
            enabled = true;
        } else if capture == "don't()" {
            enabled = false;
        } else if enabled {
            let mut splitted_mul = capture.split(",");
            let a = splitted_mul.next().unwrap();
            let b = splitted_mul.last().unwrap();
            result += a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap();
        }
    }
    return result;
}

fn main() {
    let instructions = fs::read_to_string("/Users/niklasrousset/Developer/AoC/2024/inputs/day3.txt")
        .expect("Something went wrong reading the file");

    println!("Part 1: {}", part1(instructions.as_str()));
    println!("Part 2: {}", part2(instructions.as_str()));
}