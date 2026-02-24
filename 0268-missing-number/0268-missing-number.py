class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor_all = 0
        xor_num = 0

        for num in nums:
            xor_num ^= num
        
        for i in range(len(nums)+1):
            xor_all ^= i
        
        return xor_num ^ xor_all
