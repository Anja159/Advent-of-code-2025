from functools import cache
from scripts.utils import *

input = "input.txt"
naprave= {"out": []}

for line in parse_input(input):
    deli = line.strip().split()
    zac = deli[0][:-1]   
    kon = deli[1:]
    naprave[zac] = kon

@cache
def rek(node, jedac, jefft):
    if node == "dac":
        jedac = True
    if node == "fft":
        jefft = True

    if node == "out" and jedac and jefft:
        return 1

    skupaj = 0
    for naslednj in naprave.get(node, []):
        skupaj += rek(naslednj, jedac, jefft)

    return skupaj

print(rek("svr", False, False))
