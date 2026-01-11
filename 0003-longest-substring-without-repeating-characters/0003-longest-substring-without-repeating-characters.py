class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        left = 0
        sett = set()

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            length = right - left + 1
            max_length = max(max_length, length)
        
        return max_length