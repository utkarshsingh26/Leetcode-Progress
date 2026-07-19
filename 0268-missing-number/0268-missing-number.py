class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arr = [0] * (len(nums) + 1)

        for i in range(len(arr)):
            arr[i] = i
        
        xor1, xor2= 0,0

        for num in nums:
            xor1 ^= num
        
        for a in arr:
            xor2 ^= a
        
        return xor1 ^ xor2