import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []

        count = Counter(nums)

        for key,val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [y for _,y in heap]