def read_input(f):
    file = open(f, "r")
    return file.read()


def find_position(inp, chunk):
    i = 0
    while i + chunk < len(inp):
        if len(set(inp[i : i + chunk])) == chunk:
            return i + chunk
        i += 1


if __name__ == "__main__":
    inp = read_input("input.txt")

    # part 1
    print(find_position(inp, 4))

    # part 2
    print(find_position(inp, 14))
