with open('input2.txt') as f:
    lines = f.readlines()


def get_round_score(me, opp):
    if me == "X":
        if opp == "A":
            return 3
        elif opp == "B":
            return 0
        else:
            return 6
    elif me == "Y":
        if opp == "A":
            return 6
        elif opp == "B":
            return 3
        else:
            return 0
    else:
        if opp == "A":
            return 0
        elif opp == "B":
            return 6
        else:
            return 3


score = 0
for line in lines:
    opponent_pick = line[0]
    my_pick = line[2]
    if my_pick == "X":
        score += 1
    elif my_pick == "Y":
        score += 2
    else:
        score += 3
    score += get_round_score(my_pick, opponent_pick)

print(score)

