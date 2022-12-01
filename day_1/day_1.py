def read_input(f):
    file = open(f, "r")
    return file.read()


def calculate_elf_calories(inp):
    elves = []
    cur = 0
    for line in inp:
        if line == "":
            elves.append(cur)
            cur = 0
        else:
            cur += int(line)

    return elves


if __name__ == "__main__":
    inp = read_input("input.txt").split("\n")
    elf_cals = calculate_elf_calories(inp)

    # Part 1
    print(max(elf_cals))

    # Part 2
    elf_cals = sorted(elf_cals, reverse=True)
    print(elf_cals[0] + elf_cals[1] + elf_cals[2])
