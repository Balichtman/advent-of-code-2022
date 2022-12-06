with open('input6.txt') as f:
    lines = f.readlines()

for line in lines:
    index = 0
    while index < len(line)-3:
        subset = line[index:index+4]
        uniqueCount = len(set(subset))
        if uniqueCount == 4:
            print(index+4)
            break
        index += 1
