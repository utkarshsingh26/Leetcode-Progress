class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if abs(target - closest) > abs(target - summ):
                    closest = summ
                
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                elif summ == target:
                    closest = summ
                    return closest
        
        return closest