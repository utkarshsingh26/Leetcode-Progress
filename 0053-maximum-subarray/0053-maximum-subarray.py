class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]
            max_sum = max(max_sum, summ)

            if summ < 0:
                summ = 0
        
        return max_sum