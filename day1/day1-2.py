with open('input1.txt') as f:
    lines = f.readlines()

all_sums = []
current_total = 0
for line in lines:
    if line != "\n":
        current_total += int(line)
    else:
        all_sums.append(current_total)
        current_total = 0

all_sums.sort(reverse=True)
sum_of_top_3 = 0
for s in all_sums[0:3]:
    sum_of_top_3 += s

print(sum_of_top_3)
