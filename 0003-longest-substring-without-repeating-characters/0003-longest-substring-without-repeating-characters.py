class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        sett = set()
        left = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            longer = (right - left) + 1
            longest = max(longest, longer)
        
        return longest