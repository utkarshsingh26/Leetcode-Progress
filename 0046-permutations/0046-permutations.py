class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        temp = []

        good = [False] * len(nums)

        def backtrack():
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            
            for i in range(len(nums)):
                if good[i]:
                    continue
                
                temp.append(nums[i])
                good[i] = True

                backtrack()

                temp.pop()
                good[i] = False
        
        backtrack()
        return result