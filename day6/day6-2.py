with open('input6.txt') as f:
    lines = f.readlines()

for line in lines:
    index = 0
    while index < len(line)-3:
        subset = line[index:index+14]
        uniqueCount = len(set(subset))
        if uniqueCount == 14:
            print(index+14)
            break
        index += 1
