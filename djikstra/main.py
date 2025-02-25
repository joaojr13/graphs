import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dijkstra import dijkstra

def main():
    g = nx.DiGraph()
    
    g.add_edge(0, 3, weight=20)
    g.add_edge(0, 2, weight=60)
    g.add_edge(0, 4, weight=50)

    g.add_edge(3, 4, weight=30)

    g.add_edge(2, 5, weight=90)
    g.add_edge(4, 5, weight=80)

    distances, predecessors = dijkstra(g, 0)
    print("Distâncias mínimas:", distances)
    print("Predecessores:", predecessors)

if __name__ == "__main__":
    main()