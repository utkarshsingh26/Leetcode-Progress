class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        def distance(x,y):
            return x*x + y*y

        for point in points:
            dist = distance(point[0], point[1])
            temp = [-dist, point]
            
            if len(heap) < k:
                heapq.heappush(heap, temp)
            else:
                heapq.heappushpop(heap, temp)
        
        return [y for [_,y] in heap]
