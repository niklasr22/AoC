use std::{fs, iter::zip};

fn main() {
    let contents: String = fs::read_to_string("/Users/niklasrousset/Developer/AoC/2024/inputs/day1.txt")
        .expect("Something went wrong reading the file");
    
    let lines: Vec<&str> = contents.lines().collect();

    let mut list1 = lines.iter().map(|x| x.split(" ").next().unwrap().parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let mut list2 = lines.iter().map(|x| x.split(" ").last().unwrap().parse::<i32>().unwrap()).collect::<Vec<i32>>();

    list1.sort();
    list2.sort();

    let mut diffs = 0;
    for (a, b) in zip(list1.iter(), list2.iter()) {
        diffs += (a - b).abs();
    }
    println!("Part 1: {}", diffs);

    let mut similarity_score = 0;
    for a in list1.iter() {
        similarity_score += a * list2.iter().filter(|&b| a == b).count() as i32;
    }
    println!("Part 2: {}", similarity_score);
}