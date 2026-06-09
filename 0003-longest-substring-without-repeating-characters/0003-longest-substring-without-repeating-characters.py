class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sett = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            length = right - left + 1
            max_length = max(length, max_length)
        
        return max_length