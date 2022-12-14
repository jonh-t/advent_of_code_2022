def read_input(f):
    file = open(f, "r")
    return file.read()


def split_in_half(s):
    return set(s[0 : int(len(s) / 2)]), set(s[int(len(s) / 2) : len(s)])


def find_matches(s1, s2):
    matches = s1.intersection(s2)
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
    for i in inp:
        s1, s2 = split_in_half(i)
        matches.append(*find_matches(s1, s2))

    total = 0

    for m in matches:
        total += key[m]

    print(total)
