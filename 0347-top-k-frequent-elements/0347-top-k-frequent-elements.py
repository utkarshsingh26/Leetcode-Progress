import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        heap = []

        for key,val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [val for _,val in heap]
        
        