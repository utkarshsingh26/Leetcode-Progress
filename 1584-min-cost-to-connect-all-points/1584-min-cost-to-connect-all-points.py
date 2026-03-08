import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        cost = 0
        seen = set()
        min_heap = [(0,0)]

        while len(seen) < len(points):
            distance, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            cost += distance
            xi, yi = points[i]

            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    neighbor_distance = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (neighbor_distance, j))
        
        return cost
