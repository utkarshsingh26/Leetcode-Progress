class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        temp = []

        used = [False] * len(nums)

        def backtrack():
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            
            if len(temp) > len(nums):
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                temp.append(nums[i])
                used[i] = True

                backtrack()
                temp.pop()
                used[i] = False
        
        backtrack()
        return result