class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = set()
        temp = []
        nums.sort()

        result.add(tuple(temp[:]))

        def backtrack(index):
            if index >= len(nums):
                return
            
            backtrack(index+1)

            temp.append(nums[index])
            result.add(tuple(temp[:]))

            backtrack(index+1)
            temp.pop()
        
        backtrack(0)
        return [list(t) for t in result]