import math
from itertools import combinations
#networkx my beloved :p
import networkx as nx
from scripts.utils import *

dol = 1000
def evklid(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

file = "input.txt"
parsano = []
skupaj = 0

for line in parse_input(file):
    vrstica = []
    for x in line.split(","):
        vrstica.append(int(x))
    parsano.append(tuple(vrstica))

pari = list(combinations(parsano, 2))
pari.sort(key=lambda p: evklid(p[0], p[1]))

G = nx.Graph()
G.add_edges_from(pari[:dol])

tocke = []
for g in nx.connected_components(G):
    tocke.append(len(g))

prvetri = sorted(tocke, reverse=True)[:3]
print(math.prod(prvetri))
