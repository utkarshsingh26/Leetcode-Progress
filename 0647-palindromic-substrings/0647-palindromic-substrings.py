class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expandAroundCenter(left, right):
            count = 0
            while (left >= 0 and right < len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        count = 0

        for i in range(len(s)):

            odd = expandAroundCenter(i,i)
            even = expandAroundCenter(i,i+1)

            count += (odd + even)

        return count