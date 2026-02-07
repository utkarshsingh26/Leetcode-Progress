import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        heap = []

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        for key, value in hashmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        
        return list(value for _,value in heap)
        