from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        heap = []

        for key,val in count.items():
            if len(heap) < k:
                heapq.heappush(heap,(val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [key for _,key in heap]