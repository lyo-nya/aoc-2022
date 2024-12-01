import fileinput
from re import split


def get_pairs_diff(range_pairs: str) -> list[int]:
    values = list(map(int, split("[,\-]", range_pairs)))
    return [
        values[0] - values[2],
        values[3] - values[1],
        values[2] - values[1],
        values[0] - values[3]
    ]


def solution(pairs_diff: list[int]) -> tuple[int, int]:
    # Part 1
    condition = pairs_diff[0] * pairs_diff[1]
    if condition >= 0:
        return 1, 1
    if (pairs_diff[0] <= 0) and (pairs_diff[2] <= 0):
        return 0, 1
    if (pairs_diff[2] <= 0) and (pairs_diff[3] <= 0):
        return 0, 1
    return 0, 0


part_1_result = 0
part_2_result = 0
for line in fileinput.input(files="input.txt"):
    value = line.strip()
    pairs_diff = get_pairs_diff(value)
    p1, p2 = solution(pairs_diff)
    part_1_result += p1
    part_2_result += p2

print(f"One range fully contains the other in {part_1_result} cases")
print(f"Ranges overlap at all in {part_2_result} cases")
