import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        counter = {}

        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
        
        for key,value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        
        return [value for _,value in heap]