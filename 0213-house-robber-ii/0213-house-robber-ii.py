class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def robbing(nums):

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[-1]
        
        length_of_houses = len(nums)

        scenario1 = robbing(nums[1:])
        scenario2 = robbing(nums[:length_of_houses-1])

        return max(scenario1, scenario2)


