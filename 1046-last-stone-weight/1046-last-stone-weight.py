import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            biggest = heapq.heappop(stones)
            secondBiggest = heapq.heappop(stones)

            biggest = -1 * biggest
            secondBiggest = -1 * secondBiggest

            diff = biggest - secondBiggest
            diff = -1 * diff

            heapq.heappush(stones, diff)
        
        return -stones[0]
