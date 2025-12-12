from scripts.utils import *

file = "input.txt"
whole = whole_input(file)

deli = []
for p in whole.strip().split("\n\n"):
    deli.append(p.strip())
*oblike, regije = deli  

sizes = []
for o in oblike:
    cnt = 0
    for c in o:
        if c == "#":
            cnt += 1
    sizes.append(cnt)

skupaj = 0

for vrstica in regije.splitlines():
    deli = vrstica.replace(":", " ").replace("x", " ").split()
    sir, vis, *kol = map(int, deli)

    pov = sir * vis
    pot = 0
    for i in range(len(sizes)):
        pot += kol[i] * sizes[i]

    if pov >= pot:
        skupaj += 1

print(skupaj)
