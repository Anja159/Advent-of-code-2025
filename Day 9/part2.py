from scripts.utils import *
from itertools import combinations

file = "input.txt"

tocke = []
for line in parse_input(file):
    tocke.append(tuple(map(int, line.split(","))))

robovi = list(zip(tocke, tocke[1:] + tocke[:1]))

makspl = 0

for p1, p2 in combinations(tocke, 2):
    (x1, y1), (x2, y2) = p1, p2
    xmin, xmaks = sorted((x1, x2))
    ymin, ymaks = sorted((y1, y2))

    if xmin == xmaks or ymin == ymaks:
        continue

    pravokotnik = True

    for (ax, ay), (bx, by) in robovi:
        if ay == by:
            if ymin < ay < ymaks:
                smin, smaks = sorted((ax, bx))
                if (smin <= xmin < smaks) or (smin < xmaks <= smaks):
                    pravokotnik = False
                    break

        elif ax == bx:
            if xmin < ax < xmaks:
                smin, smaks = sorted((ay, by))
                if (smin <= ymin < smaks) or (smin < ymaks <= smaks):
                    pravokotnik = False
                    break


    if not pravokotnik:
        continue

    ploscina = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
    if ploscina > makspl:
        makspl = ploscina

print(makspl)
