import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidDistance(x,y):
            return x*x + y*y
        
        heap = []

        for point in points:
            distance = euclidDistance(point[0], point[1])
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                heapq.heappushpop(heap, (-distance, point))
        
        return list((point) for (distance, point) in heap)