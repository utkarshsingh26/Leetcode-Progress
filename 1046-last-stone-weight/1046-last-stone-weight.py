import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            biggest = -1 * (heapq.heappop(stones))
            secondBiggest = -1 * (heapq.heappop(stones))
            
            difference = biggest - secondBiggest
            heapq.heappush(stones, -difference)
        
        return -stones[0]
        