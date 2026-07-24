import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0, src, 0)] # cost, node, stops
        best = {} # (node, stops) = cost

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node,stops) in best and best[(node,stops)] <= cost:
                continue
            
            best[(node,stops)] = cost

            for neighbor in graph[node]:
                new_cost = cost + neighbor[1]
                new_stops = stops + 1
                heapq.heappush(heap, (new_cost, neighbor[0], new_stops))
        
        return -1