import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for source, destination, price in flights:
            graph[source].append((destination, price))
        
        best = {} # (city, stops) = cost
        min_heap = [(0,src,0)] # cost, city, stops

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            if city == dst:
                return cost
            
            if stops > k:
                continue
            
            if (city, stops) in best and best[(city, stops)] >= cost:
                continue
            
            best[(city, stops)] = cost

            for neighbor, neighbor_cost in graph[city]:
                new_stops = stops + 1
                new_cost = cost + neighbor_cost
                heapq.heappush(min_heap, (new_cost, neighbor, new_stops))

        return -1