class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sett = set(nums)
        longest = 0
        longer = 0

        for num in sett:
            if num - 1 not in sett:
                next_num = num + 1
                longer = 1
                while next_num in sett:
                    next_num += 1
                    longer += 1
                longest = max(longer, longest)
        
        return longest