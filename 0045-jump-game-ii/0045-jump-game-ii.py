class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_jump = 0
        jumps = 0
        curr_end = 0

        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i] + i)
            
            if i == curr_end:
                jumps += 1
                curr_end = max_jump
        
        return jumps