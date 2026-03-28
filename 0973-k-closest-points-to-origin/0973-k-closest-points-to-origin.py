import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclideanDistance(x,y):
            return x*x + y*y
        
        heap = []

        for point in points:
            dist = euclideanDistance(point[0], point[1])

            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else:
                heapq.heappushpop(heap, (-dist, point))
        
        return [point for _,point in heap]
        

