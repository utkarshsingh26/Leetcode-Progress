class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distanceToOrigin(point):
            x = point[0]
            y = point[1]

            distance = x*x + y*y

            return distance
        
        heap = []

        for point in points:
            localDistance = distanceToOrigin(point)
            
            if len(heap) < k:
                heapq.heappush(heap, (-localDistance, point))
            else:
                heapq.heappushpop(heap, (-localDistance, point))
        
        return list(point for _,point in heap)