import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for source, destination, price in flights:
            graph[source].append((destination, price))
        
        best = {} # (node, flights_used) = cost
        min_heap = [(0,src,0)] # cost, node, flight_used

        while min_heap:
            cost, node, flights_used = heapq.heappop(min_heap)

            if node == dst:
                return cost
            
            if flights_used == k+1:
                continue
            
            for neighbor, neighbor_cost in graph[node]:
                new_cost = cost + neighbor_cost
                new_flights_used = flights_used + 1
                
                state = (neighbor, new_flights_used)

                if state not in best or new_cost < best[state]:
                    best[state] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor, new_flights_used))
        
        return -1