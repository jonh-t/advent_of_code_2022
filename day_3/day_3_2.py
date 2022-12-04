def read_input(f):
    file = open(f, "r")
    return file.read()


def find_matches(s1, s2, s3):
    s1 = set([char for char in s1])
    s2 = set([char for char in s2])
    s3 = set([char for char in s3])

    matches = s1.intersection(s2, s3)
    return matches


def get_key():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    idx = 1
    for c in chars:
        key[c] = idx
        idx += 1

    return key


if __name__ == "__main__":
    inp = read_input("input.txt").split("\n")
    matches = []
    key = get_key()

    idx = 0

    while idx + 2 < len(inp):
        s1, s2, s3 = inp[idx], inp[idx + 1], inp[idx + 2]
        matches.append(*find_matches(s1, s2, s3))
        idx += 3

    total = 0

    for m in matches:
        total += key[m]

    print(total)
