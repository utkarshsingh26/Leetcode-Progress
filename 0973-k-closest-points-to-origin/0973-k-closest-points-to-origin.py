class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidDistance(x,y):
            distance = x*x + y*y
            return distance
        
        heap = []

        for point in points:
            distance = euclidDistance(point[0], point[1])
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                heapq.heappushpop(heap, (-distance, point))
        
        return [point for (_,point) in heap]