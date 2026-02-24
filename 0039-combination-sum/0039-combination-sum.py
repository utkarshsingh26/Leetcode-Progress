class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        temp = []

        def backtrack(index, curr_sum):
            if curr_sum == target:
                result.append(temp[:])
                return
            
            if index >= len(candidates) or curr_sum > target:
                return
            
            backtrack(index+1, curr_sum)

            temp.append(candidates[index])
            backtrack(index, curr_sum + candidates[index])

            temp.pop()
        
        backtrack(0,0)
        return result