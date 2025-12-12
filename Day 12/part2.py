import random
import time

visina = 14
trupvisina = 3
trupsirina = 3
okraski = "o@+"
verjetnostokraska = 0.18
zamik = 0.03
seme = 2026

if seme is not None:
    random.seed(seme)

vrstice = []

for i in range(visina):
    presledki = visina - i - 1
    sirina = 2 * i + 1
    chars = ["*"] * sirina
    if i > 0 and okraski:
        for j in range(sirina):
            if random.random() < verjetnostokraska:
                chars[j] = random.choice(okraski)
    vrstice.append(" " * presledki + "".join(chars))

presledkitrup = visina - (trupsirina // 2) - 1
for _ in range(trupvisina):
    vrstice.append(" " * presledkitrup + "|" * trupsirina)

for v in vrstice:
    print(v)
    if zamik:
        time.sleep(zamik)

print()
print("AoC 2025 done (24/24)! See you in 2026 :*")
