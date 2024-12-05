use std::{cmp::Ordering, collections::HashMap, fs};

fn main() {
    let contents: String = fs::read_to_string("./2024/inputs/day5.txt")
        .expect("Something went wrong reading the file");

    let mut data_splits = contents.split("\n\n");
    let rules = data_splits
        .next()
        .unwrap()
        .lines()
        .map(|x| x.trim())
        .collect::<Vec<&str>>();

    let updates = data_splits
        .next()
        .unwrap()
        .lines()
        .map(|x| x.split(",").collect::<Vec<&str>>())
        .collect::<Vec<Vec<&str>>>();

    let mut rule_map: HashMap<&str, Vec<&str>> = HashMap::new();
    for rule in rules {
        let mut rule_split = rule.split("|");
        let key = rule_split.next().unwrap().trim();
        let value = rule_split.next().unwrap().trim();
        if rule_map.contains_key(key) {
            rule_map.get_mut(key).unwrap().push(value);
        } else {
            rule_map.insert(key, vec![value]);
        }
    }

    let mut a_mid_sum = 0;
    let mut b_mid_sum = 0;

    for update in updates {
        let mut sorted_update = update.clone();
        sorted_update.sort_by(|a, b| {
            if rule_map.contains_key(a) && rule_map[a].contains(b) {
                return Ordering::Less;
            } else {
                return Ordering::Equal;
            }
        });

        if update == sorted_update {
            a_mid_sum += update[update.len() / 2].parse::<i32>().unwrap();
        } else {
            b_mid_sum += sorted_update[update.len() / 2].parse::<i32>().unwrap();
        }
    }

    println!("A: {:?}", a_mid_sum);
    println!("B: {:?}", b_mid_sum);
}
