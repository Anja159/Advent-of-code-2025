from scripts.utils import *

file = "input.txt"
skupaj = 0

for line in parse_input(file):
    odstr = len(line) - 2
    stack = []

    for st in line:
        while odstr and stack and stack[-1] < st:
            stack.pop()
            odstr -= 1
        stack.append(st)

    if odstr > 0:
        stack = stack[:-odstr]

    value = int("".join(stack))
    skupaj += value

print(skupaj)
