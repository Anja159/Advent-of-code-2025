from scripts.utils import *

file = "input.txt"

skupaj = 50
nula = 0

for line in parse_input(file):

    # Takle mamo
    if "L" in line:
        koraki = int(line[1:])
        for i in range(koraki):
            skupaj -= 1
            if skupaj < 0:      
                skupaj %= 100
            if skupaj == 0:      
                nula += 1
    elif "R" in line:
        koraki = int(line[1:])
        for i in range(koraki):
            skupaj += 1
            if skupaj >= 100:    
                skupaj %= 100
            if skupaj == 0:      
                nula += 1

print(nula)
