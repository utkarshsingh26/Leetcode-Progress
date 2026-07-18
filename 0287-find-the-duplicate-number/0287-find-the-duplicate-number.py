class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        counter = Counter(nums)
        
        for key,val in counter.items():
            if val != 1:
                return key