class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float("-inf")
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            max_sum = max(summ, max_sum)
            if summ < 0:
                summ = 0
        
        return max_sum