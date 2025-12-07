from scripts.utils import *

file = "input.txt"
tabela = parse_grid(file)

start = tabela[0].index("S")

vsepoti = [1 for h in range(len(tabela[0]))]

for vrstica in range(len(tabela) - 1, 0, -1):
    nove = vsepoti[:]
    for stolpec in range(len(tabela[0])):
        if tabela[vrstica][stolpec] == "^":

            if stolpec - 1 >= 0:
                left = vsepoti[stolpec - 1]
            else:
                left = 1
            right = vsepoti[stolpec + 1]

            if stolpec + 1 < len(tabela[0]):
                right = vsepoti[stolpec + 1]
            else:
                right = 1
            nove[stolpec] = left + right
            
    vsepoti = nove

print(vsepoti[start])
