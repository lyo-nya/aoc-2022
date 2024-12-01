import fileinput


def get_score(letter: str) -> int:
    if letter >= "a":
        return ord(letter) - 96
    return ord(letter) - 38


def part1(value: str) -> int:
    strlen = len(value)
    first, second = value[:strlen // 2], value[strlen // 2:]
    return get_score(set(first).intersection(second).pop())


def part2(result_set: set, idx: int, value: str) -> tuple[set, int, int]:
    if not result_set:
        return result_set.union(value), 1, 0
    if idx == 1:
        return result_set.intersection(value), 2, 0
    if idx == 2:
        return set(), 0, get_score(result_set.intersection(value).pop())


part_1_score = 0
part_2_score = 0
curr_set = set()
curr_idx = 0
for line in fileinput.input(files="input.txt"):
    value = line.strip()
    # Part 1
    part_1_score += part1(value)
    # Part 2
    curr_set, curr_idx, score = part2(curr_set, curr_idx, value)
    part_2_score += score

print(f"Part 1 score is {part_1_score}")
print(f"Part 2 score is {part_2_score}")