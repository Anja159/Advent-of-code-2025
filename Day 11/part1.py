from functools import cache
from scripts.utils import *

input = "input.txt"
naprave= {"out": []}

for line in parse_input(input):
    deli = line.strip().split()
    zac = deli[0][:-1]   
    kon = deli[1:]
    naprave[zac] = kon

def rek(zac):
    skupaj = 1 if zac == "out" else 0
    for naslednj in naprave.get(zac, []):
        skupaj += rek(naslednj)
    return skupaj

print(rek("you"))
