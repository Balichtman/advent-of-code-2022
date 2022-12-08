with open('input8.txt') as f:
    lines = f.readlines()
high_score = 0
for lineNum in range(0, len(lines)):
    for charNum in range(0, len(lines[lineNum].strip("\n"))):
        top_score = 0
        right_score = 0
        bottom_score = 0
        left_score = 0
        for ln in range(lineNum-1, -1, -1):
            if lines[ln][charNum] < lines[lineNum][charNum]:
                top_score += 1
            elif lines[ln][charNum] >= lines[lineNum][charNum]:
                top_score += 1
                break
        for cn in range(charNum+1, len(lines[lineNum].strip("\n"))):
            if lines[lineNum][cn] < lines[lineNum][charNum]:
                right_score += 1
            elif lines[lineNum][cn] >= lines[lineNum][charNum]:
                right_score += 1
                break
        for ln in range(lineNum+1, len(lines)):
            if lines[ln][charNum] < lines[lineNum][charNum]:
                bottom_score += 1
            elif lines[ln][charNum] >= lines[lineNum][charNum]:
                bottom_score += 1
                break
        for cn in range(charNum-1, -1, -1):
            if lines[lineNum][cn] < lines[lineNum][charNum]:
                left_score += 1
            elif lines[lineNum][cn] >= lines[lineNum][charNum]:
                left_score += 1
                break
        tree_score = top_score * right_score * bottom_score * left_score
        if tree_score > high_score:
            high_score = tree_score
print(high_score)
