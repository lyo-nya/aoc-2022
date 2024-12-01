import fileinput

# Initialize array of zeros (top-3 elves calories)
heavy_lifters = [0] * 3

# Initialize current elf calories
curr = 0


def insert_elf(top_3_array: list, elf_calories: int):
    """
    Function, that inserts elf into top-3 if he suits
    """

    # Iterate over top-3
    for idx, lifter in enumerate(top_3_array):
        # If given elf carries more than smb from top-3
        if elf_calories >= lifter:
            # Put it on respective position
            top_3_array.insert(idx, elf_calories)
            # Drop new top-4, he's not in top-3 anymore
            top_3_array.pop(3)
            break


# Read file
for line in fileinput.input(files="input.txt"):
    value = line.strip()
    # Check if carriage of current elf if finished
    if value == "":
        # If so, add current elf to top-3 (if eligible)
        insert_elf(heavy_lifters, curr)
        # Set next elf carriage to 0
        curr = 0
        # Go to nex iteration
        continue
    # If carriage is not finished, add it to current elfs
    curr += int(value)

# Additional step to cover case, when last elf is in top-3
insert_elf(heavy_lifters, curr)

# Print out results
print(f"Elf, carrying most Calories carries: {heavy_lifters[0]}")
print(f"Top three elves are carrying: {sum(heavy_lifters)}")
