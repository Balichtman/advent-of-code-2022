with open('input9.txt') as f:
    lines = f.readlines()
h_position = [0, 0]
t_position = [0, 0]
unique_positions = []
for line in lines:
    direction = line[0]
    distance = int(line.split(" ")[1])
    for i in range(0, distance):
        match direction:
            case "U":
                h_position[1] = h_position[1] + 1
            case "D":
                h_position[1] = h_position[1] - 1
            case "L":
                h_position[0] = h_position[0] - 1
            case "R":
                h_position[0] = h_position[0] + 1
            case _:
                break
        if t_position[0] == h_position[0] and t_position[1] == h_position[1]:
            pass
        elif t_position[0] == h_position[0]:
            if abs(h_position[1] - t_position[1]) > 1:
                if h_position[1] > t_position[1]:
                    t_position[1] += 1
                else:
                    t_position[1] -= 1
        elif t_position[1] == h_position[1]:
            if abs(h_position[0] - t_position[0]) > 1:
                if h_position[0] > t_position[0]:
                    t_position[0] += 1
                else:
                    t_position[0] -= 1
        elif (abs(t_position[0]-h_position[0])) > 1 or (abs(t_position[1]-h_position[1]) > 1):
            if h_position[0] > t_position[0]:
                t_position[0] += 1
            else:
                t_position[0] -= 1
            if h_position[1] > t_position[1]:
                t_position[1] += 1
            else:
                t_position[1] -= 1
        if [t_position[0], t_position[1]] not in unique_positions:
            unique_positions.append([t_position[0], t_position[1]])
print(len(unique_positions))
