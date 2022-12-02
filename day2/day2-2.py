with open('input2.txt') as f:
    lines = f.readlines()


def get_round_score(me, opp):
    if me == "X":
        if opp == "A":
            return 3
        elif opp == "B":
            return 1
        else:
            return 2
    elif me == "Y":
        if opp == "A":
            return 4
        elif opp == "B":
            return 5
        else:
            return 6
    else:
        if opp == "A":
            return 8
        elif opp == "B":
            return 9
        else:
            return 7


score = 0
for line in lines:
    opponent_pick = line[0]
    my_pick = line[2]
    score += get_round_score(my_pick, opponent_pick)

print(score)

