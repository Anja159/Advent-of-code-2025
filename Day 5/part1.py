from scripts.utils import *

file = "input.txt"

intervali = []
skupaj = 0

for line in parse_input(file):
    
    if not line.strip():             
        continue

    if "-" in line:
        intervali.append(tuple(map(int, line.split("-"))))
    else:
        for i in range(len(intervali)):
            if int(line) >= intervali[i][0] and int(line) <= intervali[i][1]:
                skupaj += 1
                break

print(skupaj)

