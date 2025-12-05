from scripts.utils import *

file = "input.txt"

skupaj = 50
nula = 0

for line in parse_input(file):

    if "L" in line:
        skupaj -= int(line[1:])
    elif "R" in line:
        skupaj += int(line[1:])

    skupaj %= 100

    if skupaj == 0:
        nula += 1

print(nula)

