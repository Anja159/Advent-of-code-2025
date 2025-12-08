import math
from itertools import combinations
#networkx my beloved :p
import networkx as nx
from scripts.utils import *

def evklid(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

file = "input.txt"
parsano = []

for line in parse_input(file):
    vrstica = [int(x) for x in line.split(",")]
    parsano.append(tuple(vrstica))

pari = list(combinations(parsano, 2))
pari.sort(key=lambda p: evklid(p[0], p[1]))

G = nx.Graph()
G.add_nodes_from(parsano)      
for a, b in pari:
    G.add_edge(a, b)
    if nx.is_connected(G):         
        print(a[0] * b[0])     
        break
