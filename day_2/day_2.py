def read_input(f):
    file = open(f, "r")
    return file.read()


def calculate_round_part_1(opponent_choice, your_choice):
    choices = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "win": 6,
        "draw": 3,
        "lose": 0,
    }

    if choices[opponent_choice] == choices[your_choice]:
        return scores["draw"] + scores[your_choice]
    elif opponent_choice == "A" and your_choice == "Y":
        return scores["win"] + scores[your_choice]
    elif opponent_choice == "A" and your_choice == "Z":
        return scores["lose"] + scores[your_choice]
    elif opponent_choice == "B" and your_choice == "X":
        return scores["lose"] + scores[your_choice]
    elif opponent_choice == "B" and your_choice == "Z":
        return scores["win"] + scores[your_choice]
    elif opponent_choice == "C" and your_choice == "X":
        return scores["win"] + scores[your_choice]
    elif opponent_choice == "C" and your_choice == "Y":
        return scores["lose"] + scores[your_choice]
    return 0


def calculate_round_part_2(opponent_choice, your_choice):
    winning_choices = {"A": "B", "B": "C", "C": "A"}
    losing_choices = {"A": "C", "B": "A", "C": "B"}

    scores = {
        "A": 1,
        "B": 2,
        "C": 3,
        "win": 6,
        "draw": 3,
        "lose": 0,
    }

    if your_choice == "X":
        return scores["lose"] + scores[losing_choices[opponent_choice]]
    elif your_choice == "Y":
        return scores["draw"] + scores[opponent_choice]
    elif your_choice == "Z":
        return scores["win"] + scores[winning_choices[opponent_choice]]
    return 0


if __name__ == "__main__":
    inp = read_input("input.txt").split("\n")
    part_1_points = []
    part_2_points = []
    for line in inp:
        opponent_choice = line.split(" ")[0]
        your_choice = line.split(" ")[1]
        part_1_points.append(calculate_round_part_1(opponent_choice, your_choice))
        part_2_points.append(calculate_round_part_2(opponent_choice, your_choice))

    # part 1
    print(sum(part_1_points))

    # part 2
    print(sum(part_2_points))
