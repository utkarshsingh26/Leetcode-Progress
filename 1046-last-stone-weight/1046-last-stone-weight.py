import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
            heapq.heappush(heap, stones[i])
        
        while len(heap) >= 2:
            biggest = -1 * heapq.heappop(heap)
            secondBiggest = -1 * heapq.heappop(heap)

            diff = biggest - secondBiggest
            diff = -1 * diff

            heapq.heappush(heap, diff)
        
        return -heap[0]