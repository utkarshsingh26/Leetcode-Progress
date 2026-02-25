class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = set()
        temp = []

        result.add(tuple(temp[:]))

        def backtrack(index):
            if index >= len(nums) or len(temp) > len(nums):
                return
            
            backtrack(index+1)

            temp.append(nums[index])
            result.add(tuple(temp[:]))

            backtrack(index+1)
            temp.pop()
        
        backtrack(0)
        return list(result)