with open('input8.txt') as f:
    lines = f.readlines()
visible_trees = 0
for lineNum in range(0, len(lines)):
    for charNum in range(0, len(lines[lineNum].strip("\n"))):
        if lineNum == 0 or lineNum == len(lines)-1 or charNum == 0 or charNum == len(lines[lineNum].strip("\n"))-1:
            visible_trees += 1
        else:
            top_visible = True
            right_visible = True
            bottom_visible = True
            left_visible = True
            for ln in range(0, lineNum):
                if lines[ln][charNum] >= lines[lineNum][charNum]:
                    top_visible = False
                    break
            if not top_visible:
                for cn in range(charNum+1, len(lines[lineNum].strip("\n"))):
                    if lines[lineNum][cn] >= lines[lineNum][charNum]:
                        right_visible = False
                        break
                if not right_visible:
                    for ln in range(lineNum+1, len(lines)):
                        if lines[ln][charNum] >= lines[lineNum][charNum]:
                            bottom_visible = False
                            break
                    if not bottom_visible:
                        for cn in range(0, charNum):
                            if lines[lineNum][cn] >= lines[lineNum][charNum]:
                                left_visible = False
                                break
            if top_visible or right_visible or bottom_visible or left_visible:
                visible_trees += 1
print(visible_trees)
