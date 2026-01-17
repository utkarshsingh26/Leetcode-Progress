class Solution:
    def jump(self, nums: List[int]) -> int:

        max_jumps = 0
        curr_end = 0
        jumps = 0

        for i in range(len(nums)-1):
            max_jumps = max(max_jumps, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = max_jumps
        
        return jumps