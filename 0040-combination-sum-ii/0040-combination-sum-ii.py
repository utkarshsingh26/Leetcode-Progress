class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []
        temp = []

        def backtrack(index, curr_sum):
            if curr_sum == target:
                result.append(temp[:])
                return
            
            if index >= len(candidates) or curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                temp.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i])
                temp.pop()
        
        backtrack(0,0)
        return result