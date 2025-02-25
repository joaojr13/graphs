from extract_min import extract_min
from decrease_key import decrease_key
from relax import relax

def dijkstra(graph, source):
    # Inicialização
    dist = {node: float('inf') for node in graph.nodes}
    prev = {node: None for node in graph.nodes}
    dist[source] = 0
    
    # Fila de prioridade (min-heap)
    priority_queue = [(0, source)]  # (distância, nó)
    
    while priority_queue:
        u = extract_min(priority_queue, dist)
        if u is None:
            break
        
        for v in graph.neighbors(u):
            if relax(u, v, graph[u][v]['weight']):
                decrease_key(priority_queue, v, graph[v]['d'])

            weight = graph[u][v]['weight']
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                decrease_key(priority_queue, v, alt)
    
    return dist, prev