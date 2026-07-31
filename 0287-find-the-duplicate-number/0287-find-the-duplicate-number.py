class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        slow = nums[0]

        for _ in range(len(nums)):
            slow = nums[slow]
            fast = nums[fast]
        
        return nums[slow]