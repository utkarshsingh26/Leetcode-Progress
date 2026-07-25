class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandFromCenter(left, right):
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        
        longest = ""

        for i in range(len(s)):
            odd = expandFromCenter(i,i)
            even = expandFromCenter(i, i+1)

            longer = odd if len(odd) > len(even) else even
            longest = longest if len(longest) > len(longer) else longer
        
        return longest