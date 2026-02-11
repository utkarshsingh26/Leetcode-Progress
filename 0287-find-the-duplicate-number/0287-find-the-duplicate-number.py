from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        for key,value in counter.items():
            if value > 1:
                return key
