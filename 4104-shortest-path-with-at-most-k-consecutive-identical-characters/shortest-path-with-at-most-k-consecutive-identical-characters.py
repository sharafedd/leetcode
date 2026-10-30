import heapq
from collections import defaultdict 

class Solution(object):
    # Djikstra to algorith mto find the shortest path
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int                    number of nodes
        :type edges: List[List[int]]    edges
        :type labels: str               labels
        :type k: int                    most consecutive identical
        :rtype: int
        """
    
        adjacency_list = defaultdict(list)
        for u, v, w in edges:
            adjacency_list[u].append((v, w))

        INF = float('inf')
        
        distance = {(0, 1): 0}
        pq = [(0, 0, 1)]

        while pq:

            cost, u, run = heapq.heappop(pq)

            if cost > distance.get((u, run), INF):
                continue

            if u == n - 1:
                return cost

            for v, w in adjacency_list[u]:

                if labels[v] == labels[u]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run > k:
                    continue
                
                new_cost = cost + w

                if new_cost < distance.get((v, new_run), INF):
                    distance[(v, new_run)] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_run))

        return -1

        