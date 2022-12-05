from collections import deque


def read_input(f):
    file = open(f, "r")
    return file.read()


def crates_to_stack(crates):
    crate_rows = crates.split("\n")
    i = len(crate_rows) - 2
    num_of_columns = int([n for n in crate_rows[i + 1].split(" ") if n != ""][-1])
    crate_cols = {}
    for n in range(num_of_columns):
        crate_cols[n + 1] = deque()

    crate_rows_parsed = []

    while i >= 0:
        crates_in_row = [
            n.replace("[", "").replace("]", "") for n in crate_rows[i].split(" ")
        ]
        crate_rows_parsed.append(crates_in_row)
        i -= 1

    for row in crate_rows_parsed:
        spaces = 0
        row_index = 1
        for char in row:
            if char != "":
                crate_cols[row_index].append(char)
                row_index += 1
            elif char == "" and spaces < 3:
                spaces += 1
            elif char == "" and spaces == 3:
                spaces = 0
                row_index += 1

    return crate_cols


def parse_instructions(stacks, instructions):
    instructions = instructions.split("\n")
    for instruction in instructions:
        move_count = int(instruction.split(" ")[1])
        move_from = int(instruction.split(" ")[3])
        move_to = int(instruction.split(" ")[5])

        for i in range(move_count):
            crate = stacks[move_from].pop()
            stacks[move_to].append(crate)

    return stacks


def get_top_crate(stacks):
    top_crate_string = ""
    for k in stacks:
        top_crate_string += stacks[k][-1]

    return top_crate_string


if __name__ == "__main__":
    inp = read_input("input.txt")
    crates = inp.split("\n\n")[0]
    instructions = inp.split("\n\n")[1]
    stacks = crates_to_stack(crates)
    moved_stacks = parse_instructions(stacks, instructions)
    top_crates = get_top_crate(moved_stacks)
    print(top_crates)
