import heapq

def extract_min(priority_queue, dist):
    while priority_queue:
        d, u = heapq.heappop(priority_queue)
        if d == dist[u]:
            return u
    return None