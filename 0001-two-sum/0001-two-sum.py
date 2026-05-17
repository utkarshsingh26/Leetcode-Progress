class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        graph = {}

        for i in range(len(nums)):
            graph[nums[i]] = i
        
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in graph:
                if i != graph[toFind]:
                    return [i, graph[toFind]]