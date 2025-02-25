import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bellman_ford import bellman_ford_alg

def extract_path(G, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = G.nodes[current]['pi']
    path.reverse()
    return path

def main():
    G = nx.DiGraph()

    G.add_edge(0, 1, weight=4) #A -> B
    G.add_edge(0, 2, weight=2) #A -> D

    G.add_edge(1, 3, weight=2) #B -> C
    G.add_edge(1, 2, weight=3) #B -> D
    G.add_edge(1, 4, weight=3) #B -> E
    
    G.add_edge(2, 1, weight=1) #D -> B
    G.add_edge(2, 3, weight=4) #D -> C
    G.add_edge(2, 4, weight=5) #D -> E
    
    G.add_edge(4, 3, weight=-5) #E -> C

    pos = {
        0: (0, 0),
        1: (1, 2),
        2: (1, -2),
        3: (3, 2),
        4: (3, -2)
    }

    source = 0
    bool = bellman_ford_alg(G, source)
    
    if bool:
        print(f"Shortest distances from node {source}:")
        for node in G.nodes:
            print(f"Node {node}: {G.nodes[node]['d']}")

    else:
        print("Graph contains a negative-weight cycle")

    plt.figure(1)
    nx.draw_networkx(G, pos=pos, with_labels=True)
    
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    
    plt.show()

if __name__ == "__main__":
    main()