def read_input(f):
    file = open(f, "r")
    return file.read()


def split_pairs(pair):
    return pair.split(",")


def check_pairs(pair):
    num_1_start = int(pair[0].split("-")[0])
    num_1_end = int(pair[0].split("-")[1])
    num_2_start = int(pair[1].split("-")[0])
    num_2_end = int(pair[1].split("-")[1])

    if num_1_start >= num_2_start and num_1_start <= num_2_end:
        return True
    if num_2_start >= num_1_start and num_2_start <= num_1_end:
        return True
    return False


if __name__ == "__main__":
    inp = read_input("input.txt")
    pairs = [split_pairs(pair) for pair in inp.split("\n")]
    overlapping = [check_pairs(pair) for pair in pairs]
    print(len(list(filter(lambda i: i is True, overlapping))))
