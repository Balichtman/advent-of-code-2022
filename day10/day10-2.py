with open('input10.txt') as f:
    lines = f.readlines()
x = 1
cycle = 1


def do_cycle():
    global cycle
    global signal_strengths
    if cycle == x or cycle == x+2 or cycle == x+1:
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1
    if cycle == 41:
        print("")
        cycle = 1


for line in lines:
    instruction = line.split(" ")[0].strip("\n")
    if instruction == "addx":
        value = line.split(" ")[1]
        do_cycle()
        do_cycle()
        x += int(value)
    elif instruction == "noop":
        do_cycle()

