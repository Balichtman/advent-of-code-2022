with open('input4.txt') as f:
    lines = f.readlines()

sumOfContainedPairs = 0
for line in lines:
    elf_1 = line.split(",")[0]
    elf_2 = line.split(",")[1]
    elf_1_start = int(elf_1.split("-")[0])
    elf_1_end = int(elf_1.split("-")[1])
    elf_2_start = int(elf_2.split("-")[0])
    elf_2_end = int(elf_2.split("-")[1])
    if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
        sumOfContainedPairs += 1
    elif elf_2_start >= elf_1_start and elf_2_end <= elf_1_end:
        sumOfContainedPairs += 1

print(sumOfContainedPairs)