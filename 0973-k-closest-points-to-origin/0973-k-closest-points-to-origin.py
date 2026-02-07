import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x,y):
            return x*x + y*y
        
        heap = []

        for point in points:
            dist = distance(point[0], point[1])
            temp = [-dist, point[0], point[1]]
            
            if len(heap) < k:
                heapq.heappush(heap, temp)
            else:
                heapq.heappushpop(heap, temp)
        
        return [[x,y] for [_,x,y] in heap]