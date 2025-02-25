import heapq

def decrease_key(priority_queue, node, new_distance):
    heapq.heappush(priority_queue, (new_distance, node))