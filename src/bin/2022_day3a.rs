use std::fs;

fn main() {
    let contents = fs::read_to_string("./2022/inputs/day3.txt").expect("File reading error");
    let lines = contents.lines().map(|l| -> String { l.into() });
    let priorities = lines.map(search_compartments);
    let s: i32 = priorities.sum();
    println!("Priorities: {}", s)
}

fn search_compartments(rucksack: String) -> i32 {
    let mid = rucksack.len() / 2;
    for i in 0..mid {
        let item = rucksack.chars().nth(i).expect("Fail");
        if rucksack[mid..].contains(item) {
            return get_priority(item).into();
        }
    }
    0
}

fn get_priority(item: char) -> u8 {
    let c = item as u8;
    if c <= 'Z' as u8 {
        return c - 'A' as u8 + 27;
    }
    return c - 'a' as u8 + 1;
}
