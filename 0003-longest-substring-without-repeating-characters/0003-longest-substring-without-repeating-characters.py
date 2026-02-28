class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        longest = 0
        sett = set()

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            length = (right - left) + 1
            longest = max(longest, length)
        
        return longest