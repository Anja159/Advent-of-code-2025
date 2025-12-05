from scripts.utils import *

file = "input.txt"

intervali = []
zdruzeni = []
skupaj = 0

for line in parse_input(file):
    
    if not line.strip():             
        continue

    if "-" in line:
        intervali.append(tuple(map(int, line.split("-"))))

for interval in sorted(intervali):

    if not zdruzeni:
        zdruzeni.append(interval)
    elif zdruzeni[-1][1] < interval[0]:
        zdruzeni.append(interval)
    else:
        zdruzeni[-1] = (zdruzeni[-1][0], max(zdruzeni[-1][1], interval[1]))

print(sum(e - s + 1 for s, e in zdruzeni))