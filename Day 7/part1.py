from scripts.utils import *

file = "input.txt"
tabela = parse_grid(file)
skupaj = 0

for vrstica in range(len(tabela)):
    for stolpec in range(len(tabela[0])):

        if tabela[vrstica][stolpec] in ("S", "|"):
            if vrstica + 1 >= len(tabela):
                continue

            if tabela[vrstica + 1][stolpec] == "^":
                if stolpec - 1 >= 0:
                    tabela[vrstica + 1][stolpec - 1] = "|"
                    skupaj += 1
                if stolpec + 1 < len(tabela[0]):
                    tabela[vrstica + 1][stolpec + 1] = "|"
            else:
                tabela[vrstica + 1][stolpec] = "|"

print(skupaj)

