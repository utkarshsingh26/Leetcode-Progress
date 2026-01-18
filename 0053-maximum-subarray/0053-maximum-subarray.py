class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        max_sum = float("-inf")
        add = 0

        for num in nums:
            add += num
            max_sum = max(max_sum, add)

            if add < 0:
                add = 0
        
        return max_sum