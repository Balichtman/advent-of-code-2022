with open('input1.txt') as f:
    lines = f.readlines()

highest = 0
current_total = 0
for line in lines:
    if line != "\n":
        current_total += int(line)
    else:
        if current_total > highest:
            highest = current_total
        current_total = 0

print(highest)
