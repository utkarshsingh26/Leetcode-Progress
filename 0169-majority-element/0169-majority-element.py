class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        majority_count = 0
        majority = float("-inf")
        
        for key,val in count.items():
            if val > majority_count:
                majority_count = val
                majority = key
        
        return majority