class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        max_jump = 0
        curr_end = 0

        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = max_jump
        
        return jumps