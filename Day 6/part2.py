from scripts.utils import parse_input
from math import prod

filename = "input.txt"
skupaj = 0
tabela = []

for line in parse_input(filename):
    tabela.append(list(line.rstrip("\n")))

sirina = max(len(vrstica) for vrstica in tabela)
for i, vrstica in enumerate(tabela):
    tabela[i] = vrstica + [" "] * (sirina - len(vrstica))

tabela = list(zip(*tabela))  

stevila = []
op = "+"

for stolpec in reversed(tabela):
    if all(c == " " for c in stolpec):
        
        if op == "*":
            vsotaprodukt = prod(stevila)
        else:
            vsotaprodukt = sum(stevila)
        skupaj += vsotaprodukt
        stevila = []
        op = "+"
        continue

    if stolpec[-1] in "+*":
        op = stolpec[-1]

    znakci = [c for c in stolpec[:-1] if c.isdigit()]
    if znakci:
        stevila.append(int("".join(znakci)))

if op == "*":
    vsotaprodukt = prod(stevila)
else:
    vsotaprodukt = sum(stevila)
skupaj += vsotaprodukt

print(skupaj)
