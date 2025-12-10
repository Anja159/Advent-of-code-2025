from scripts.utils import *
from pulp import *

datoteka = "input.txt"
skupaj = 0

for line in parse_input(datoteka):
    if not line.strip():
        continue

    vzorec, *tekst, konec = line.split()

    gumbi = []
    for gumbeki in tekst:
        notranjost = gumbeki[1:-1]          
        ind = notranjost.split(",")  
        gumb = [int(i) for i in ind]
        gumbi.append(gumb)

    koncnost = tuple(map(int, konec.strip("{}").split(",")))
    n = len(koncnost)

    prispevki = []
    for indeksi in gumbi:
        indeksi = set(indeksi)
        vrstica = []
        for i in range(n):
            vrstica.append(int(i in indeksi))
        prispevki.append(vrstica)

    model = LpProblem("aaaaaa", LpMinimize)

    pritiski = []
    for i in range(len(prispevki)):
        pritiski.append(LpVariable(f"b{i}", cat="Integer", lowBound=0))

    model += lpSum(pritiski)
    izrazi = [0] * n
    for g, prispevek in enumerate(prispevki):
        for poz, coef in enumerate(prispevek):
            if coef:
                izrazi[poz] += pritiski[g] * coef

    for poz, expr in enumerate(izrazi):
        model += (expr == koncnost[poz], f"p{poz}")

    model.solve(PULP_CBC_CMD(msg=0))

    for v in pritiski:
        skupaj += int(v.varValue)

print(skupaj)
