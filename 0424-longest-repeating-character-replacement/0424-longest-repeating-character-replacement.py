class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0
        window = {}
        max_freq = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            max_freq = max(max_freq, window[s[right]])

            if (right - left + 1) - max_freq > k:
                window[s[left]] = window.get(s[left], 0) - 1
                left += 1
            
            longest = max(longest, (right - left + 1))
        
        return longest