def read_input(f):
    file = open(f, "r")
    return file.read()


def split_in_half(s):
    return s[0 : int(len(s) / 2)], s[int(len(s) / 2) : len(s)]


def find_matches(s1, s2, s3):
    chars = {}
    for s in s1:
        chars[s] = {1}

    for s in s2:
        if s in chars.keys():
            chars[s].add(2)
        else:
            chars[s] = {2}

    for s in s3:
        if s in chars.keys():
            chars[s].add(3)
        else:
            chars[s] = {3}

    matches = []
    for k in chars:
        if len(chars[k]) > 2:
            matches.append(k)

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
