class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            toFind = target - nums[i]

            if toFind in hashmap and i != hashmap[toFind]:
                return [i, hashmap[toFind]]
