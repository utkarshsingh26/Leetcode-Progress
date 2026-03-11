class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for source, destination, price in flights:
            graph[source].append((destination, price))
        
        min_heap = [(0,src,0)] # cost, node, stops
        best = {} # (node, stops) = cost

        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            
            best[(node, stops)] = cost

            for neighbor, neighbor_cost in graph[node]:
                new_cost = cost + neighbor_cost
                new_stops = stops + 1
                heapq.heappush(min_heap, (new_cost, neighbor, new_stops))
        
        return -1