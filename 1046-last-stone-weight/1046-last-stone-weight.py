import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)
        
        while len(stones) >= 2:
            biggest = heapq.heappop(stones)
            second_biggest = heapq.heappop(stones)
            interim = (-1 * biggest) - (-1 * second_biggest)
            interim = -1 * interim
            heapq.heappush(stones, interim)
        
        return -1 * stones[0]