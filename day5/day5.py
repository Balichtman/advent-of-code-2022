with open('input5.txt') as f:
    lines = f.readlines()

stack = []
for j in range(0, 9):
    stack.append([])

lineCount = 0
for line in lines:
    if line != "\n" and lineCount < 9:
        position = 0
        for i in range(0, len(line), 4):
            if line[i] == "[":
                stack[position].append(line[i+1])
            position += 1
    if lineCount == 9:
        for s in stack:
            s.reverse()
    if lineCount > 9 and line != "\n":
        motion = line.replace("move ", "").replace(" from", "").replace(" to", "").replace(" ", ",")
        for x in range(0, int(motion.split(",")[0])):
            itemToMove = stack[int(motion.split(",")[1])-1].pop()
            stack[int(motion.split(",")[2])-1].append(itemToMove)
    lineCount += 1

for s in stack:
    print(s[len(s)-1], end="")
