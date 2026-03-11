import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclid_distance(x,y):
            return x*x + y*y
        
        heap = []

        for point in points:
            distance = euclid_distance(point[0], point[1])
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point[0], point[1]))
            else:
                heapq.heappushpop(heap, (-distance, point[0], point[1]))
        
        return [(x,y) for z,x,y in heap]
        

