import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Prim's Algorithm
        cost = 0
        seen = set()
        heap = [(0,0)] # distance, ith point from points -> we're ar distance 0 from point 0 here

        while len(seen) < len(points):
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            xi, yi = points[i]
            cost += dist

            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    neighbor_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (neighbor_dist, j))
        
        return cost