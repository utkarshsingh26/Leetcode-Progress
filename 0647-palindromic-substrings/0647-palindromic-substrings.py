class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            count += odd
            count += even
        
        return count