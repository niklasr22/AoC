import aocutils

input = aocutils.read_file("./2022/inputs/day6.txt")


def first_occurence_of_x_distinct_chars(input: str, x: int):
    for i in range(x, len(input)):
        if len(set(input[i - x + 1 : i + 1])) == x:
            return i


print("a", first_occurence_of_x_distinct_chars(input, 4))
print("b", first_occurence_of_x_distinct_chars(input, 14))
