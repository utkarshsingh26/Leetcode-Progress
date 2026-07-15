import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        result = []

        for key,val in count.items():
            if len(result) < k:
                heapq.heappush(result, (val, key))
            else:
                heapq.heappushpop(result, (val, key))
        
        return [key for _,key in result]