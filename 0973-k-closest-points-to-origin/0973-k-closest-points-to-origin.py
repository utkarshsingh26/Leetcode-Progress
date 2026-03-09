import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x,y):
            return x*x + y*y
        
        heap = []

        for point in points:
            d = distance(point[0], point[1])

            if len(heap) < k:
                heapq.heappush(heap, (-d, point))
            else:
                heapq.heappushpop(heap, (-d, point))
        print(heap)
        return list([point for (_,point) in heap])