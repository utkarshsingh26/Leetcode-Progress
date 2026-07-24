import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        seen = set()
        cost = 0
        heap = [(0,0)] # dist to node, node

        while len(seen) < len(points):
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            cost += dist
            xi, yi = points[i]

            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    new_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap, (new_dist, j))
        
        return cost
