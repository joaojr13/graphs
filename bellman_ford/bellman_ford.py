from relax import relax 
from initialize_single_source import initialize_single_source

def bellman_ford_alg(G, s):
    initialize_single_source(G, s)

    for _ in range(len(G.nodes) - 1):
        for u, v, data in G.edges(data=True):
            relax(G.nodes[u], G.nodes[v], data['weight'])
    
    for u, v, data in G.edges(data=True):
        w = data['weight']
        if G.nodes[v]['d'] > G.nodes[u]['d'] + w:
            return False

    return True