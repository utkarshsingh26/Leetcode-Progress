class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        sett = set(nums)

        return not len(sett) == len(nums)