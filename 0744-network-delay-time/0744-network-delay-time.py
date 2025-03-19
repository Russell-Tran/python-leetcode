"""
Looks like a Dijkstra 
"""

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Setup
        pq = []
        # distances = defaultdict(lambda: float('inf')) # node -> shortest distance
        distances = {node : float('inf') for node in range(1, n+1)} # node -> shortest distance
        index = defaultdict(list) # node -> [(neighbor, cost), ...]

        # Goal: Return the time which is the maximum of the 
        # {minimum distances from the origin to each respective node}


        for time in times:
            u, v, w = time
            index[u].append((v, w))

        origin = k
        distances[origin] = 0
        heapq.heappush(pq, (0, origin))

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue

            neighbors = index[node]
            for neighbor_node, weight in neighbors:
                distance_cost = distances[node] + weight
                if distance_cost < distances[neighbor_node]:
                    distances[neighbor_node] = distance_cost
                    heapq.heappush(pq, (distance_cost, neighbor_node))

        maximum_distance = max(distances.values())
        return maximum_distance if maximum_distance != float('inf') else -1



