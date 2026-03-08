import heapq
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        graph = defaultdict(list)

        for x,y,time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))
        
        best = {} # (node, time) = cost
        min_heap = [(passingFees[0], 0, 0)] # cost, node, time

        while min_heap:
            cost, node, time = heapq.heappop(min_heap)

            if node == len(passingFees)-1:
                return cost
            
            if time >= maxTime:
                continue
            
            if (node, time) in best and best[(node, time)] <= cost:
                continue
            
            best[(node, time)] = cost

            for neighbor, neighbor_time in graph[node]:
                new_cost = cost + passingFees[neighbor]
                new_time = time + neighbor_time

                if new_time <= maxTime:
                    heapq.heappush(min_heap, (new_cost, neighbor, new_time))
        
        return -1