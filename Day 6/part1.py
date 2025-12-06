from scripts.utils import parse_input
from math import prod

filename = "input.txt"
skupaj = 0
tabela = []

for line in parse_input(filename):
    tabela.append(line.split())

tabela = list(zip(*tabela))

for stolpec in tabela:
    stevila = [int(x) for x in stolpec[:-1]]
    if "*" in stolpec:
        vsotaprodukt = prod(stevila)
    else:
        vsotaprodukt = sum(stevila)
    skupaj += vsotaprodukt

print(skupaj)


