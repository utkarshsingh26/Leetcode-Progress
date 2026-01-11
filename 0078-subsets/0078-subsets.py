class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        temp = []

        result.append(temp[:])
        
        def backtrack(index):
            if index >= len(nums) or len(temp) == len(nums):
                return
            
            backtrack(index+1)

            temp.append(nums[index])
            result.append(temp[:])
            backtrack(index+1)
            temp.pop()
        
        backtrack(0)
        return result