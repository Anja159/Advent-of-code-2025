from scripts.utils import *

file = "input.txt"
makspl = 0

tocke = []

for line in parse_input(file):
    tocke.append(tuple(map(int, line.split(","))))

for i in range(len(tocke)):
    x1, y1 = tocke[i]
    for j in range(i, len(tocke)):   
        x2, y2 = tocke[j]
        ploscina = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        makspl = max(makspl, ploscina)

print(makspl)
