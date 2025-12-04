from scripts.utils import *

file = "input.txt"
skupaj = 0

tabela = parse_grid(file)

for l in range(0,100):
    for i in range(len(tabela)):
        for j in range(len(tabela[0])):
            a = get_neighbors(i, j, tabela, True)
            rolice = a.count('@')
            if rolice < 4 and tabela[i][j] == '@':
                skupaj += 1 
                tabela[i][j] = '.'

print(skupaj)
