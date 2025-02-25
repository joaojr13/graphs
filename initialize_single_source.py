def initialize_single_source(G, s):
    for node in G.nodes:
        G.nodes[node]['d'] = float("inf")
        G.nodes[node]['pi'] = None
    G.nodes[s]['d'] = 0