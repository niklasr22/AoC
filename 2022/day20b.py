import aocutils

file = {
    i: x
    for i, x in enumerate(
        aocutils.read_lines("./2022/inputs/day20.txt", lambda x: int(x) * 811589153)
    )
}

decrypted_file = list(file.keys())


def mix():
    for k, v in file.items():
        previous_index = decrypted_file.index(k)
        decrypted_file.remove(k)
        new_index = (previous_index + v) % len(decrypted_file)
        if new_index == 0:
            new_index = len(decrypted_file)
        decrypted_file.insert(new_index, k)


for _ in range(10):
    mix()

zero_key = -1
for k, v in file.items():
    if v == 0:
        zero_key = k
zero_index = decrypted_file.index(zero_key)
print(
    file[decrypted_file[(zero_index + 1000) % len(decrypted_file)]]
    + file[decrypted_file[(zero_index + 2000) % len(decrypted_file)]]
    + file[decrypted_file[(zero_index + 3000) % len(decrypted_file)]]
)
