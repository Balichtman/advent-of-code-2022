with open('input9.txt') as f:
    lines = f.readlines()
positions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
unique_positions = []
for line in lines:
    direction = line[0]
    distance = int(line.split(" ")[1])
    for i in range(0, distance):
        match direction:
            case "U":
                positions[0][1] = positions[0][1] + 1
            case "D":
                positions[0][1] = positions[0][1] - 1
            case "L":
                positions[0][0] = positions[0][0] - 1
            case "R":
                positions[0][0] = positions[0][0] + 1
            case _:
                break
        for p in range(1, len(positions)):
            if positions[p][0] == positions[p-1][0] and positions[p][1] == positions[p-1][1]:
                pass
            elif positions[p][0] == positions[p-1][0]:
                if abs(positions[p-1][1] - positions[p][1]) > 1:
                    if positions[p-1][1] > positions[p][1]:
                        positions[p][1] += 1
                    else:
                        positions[p][1] -= 1
            elif positions[p][1] == positions[p-1][1]:
                if abs(positions[p-1][0] - positions[p][0]) > 1:
                    if positions[p-1][0] > positions[p][0]:
                        positions[p][0] += 1
                    else:
                        positions[p][0] -= 1
            elif (abs(positions[p][0]-positions[p-1][0])) > 1 or (abs(positions[p][1]-positions[p-1][1]) > 1):
                if positions[p-1][0] > positions[p][0]:
                    positions[p][0] += 1
                else:
                    positions[p][0] -= 1
                if positions[p-1][1] > positions[p][1]:
                    positions[p][1] += 1
                else:
                    positions[p][1] -= 1
        if [positions[9][0], positions[9][1]] not in unique_positions:
            unique_positions.append([positions[9][0], positions[9][1]])
print(len(unique_positions))
