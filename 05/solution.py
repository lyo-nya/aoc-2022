import fileinput


def parse_creates_line(line: str):
    crates = []
    while line:
        crate, line = line[:3], line[4:]
        crates.append(crate.strip())
    return crates


def add_to_stacks(stacks: dict, crates: list) -> None:
    for idx, crate in enumerate(crates):
        if crate == "":
            continue
        crate = crate[1]
        stacks[idx + 1] = stacks.get(idx + 1, []) + [crate]


def read_instruction(line: str) -> tuple[int, int, int]:
    instruction = line.split(" ")
    q = int(instruction[1])
    source = int(instruction[3])
    target = int(instruction[-1])
    return source, target, q


def move_crates_part_1(stacks: dict, source: int, target: int, q: int):
    for _ in range(q):
        crate = stacks[source].pop(0)
        stacks[target] = [crate] + stacks.get(target, [])


def move_crates_part_2(stacks: dict, source: int, target: int, q: int):
    source_stack = stacks.pop(source, [])
    crates, stacks[source] = source_stack[:q], source_stack[q:]
    stacks[target] = crates + stacks.get(target, [])


part_1_result = {}
part_2_result = {}
instructions = False
for line in fileinput.input(files="input.txt"):
    value = line.strip()
    if value == "":
        instructions = True
        continue
    if value[0] == "1":
        continue
    if not instructions:
        crates = parse_creates_line(value)
        add_to_stacks(part_1_result, crates)
        add_to_stacks(part_2_result, crates)
    else:
        instructions = read_instruction(value)
        move_crates_part_1(part_1_result, *instructions)
        move_crates_part_2(part_2_result, *instructions)

print("Part 1 answer is " + "".join([part_1_result.get(i, [""])[0] for i in range(1, 10)]))
print("Part 2 answer is " + "".join([part_2_result.get(i, [""])[0] for i in range(1, 10)]))
