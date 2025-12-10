from scripts.utils import *
from collections import deque

datoteka = "input.txt"
skupaj = 0

for line in parse_input(datoteka):
    if not line.strip():
        continue

    vzorec, *tekst, konec = line.split()

    gumbi = [
        [int(i) for i in gumbeki[1:-1].split(",")]
        for gumbeki in tekst
    ]

    cilj = tuple(c == "#" for c in vzorec[1:-1])
    zacetek = tuple(False for _ in cilj)

    q = deque()
    q.append((zacetek, 0))
    obiskani = {zacetek}

    while q:
        stanje, razdalja = q.popleft()

        if stanje == cilj:
            skupaj += razdalja
            break

        for gumb in gumbi:
            novo = list(stanje)
            for i in gumb:
                novo[i] = not novo[i]
            t = tuple(novo)

            if t not in obiskani:
                obiskani.add(t)
                q.append((t, razdalja + 1))

print(skupaj)
