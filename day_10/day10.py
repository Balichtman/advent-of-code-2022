with open('input10.txt') as f:
    lines = f.readlines()
x = 1
cycle = 1
signal_strengths = []
interesting_signals = [20, 60, 100, 140, 180, 220]
count = 0


def do_cycle():
    global cycle
    global signal_strengths
    if cycle in interesting_signals:
        signal_strengths.append(cycle * x)
    cycle += 1


for line in lines:
    instruction = line.split(" ")[0].strip("\n")
    if instruction == "addx":
        value = line.split(" ")[1]
        do_cycle()
        do_cycle()
        x += int(value)
    elif instruction == "noop":
        do_cycle()
signal_sum = 0
for s in signal_strengths:
    signal_sum += s
print(signal_sum)
