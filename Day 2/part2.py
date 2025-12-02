from scripts.utils import *

import re

pattern = re.compile(r'^(\d+)\1+$')  

file = "input.txt"
whole = list(whole_input(file))

skupaj = 0

for line in parse_input(file):
    for part in line.split(","):
        for i in range(int(part.split("-")[0]), int(part.split("-")[1]) + 1):
            if pattern.fullmatch(str(i)):
                skupaj += i

print(skupaj)

            