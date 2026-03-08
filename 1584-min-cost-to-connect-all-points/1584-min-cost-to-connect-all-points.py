import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        seen = set()
        min_heap = [(0,0)] # distance for source to node, node
        cost = 0

        while len(seen) < len(points):
            distance, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            xi, yi = points[i]
            cost += distance

            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    new_distance = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (new_distance, j))
        
        return cost