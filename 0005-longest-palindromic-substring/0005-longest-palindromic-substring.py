class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""

        def expandAroundCentre(left,right):
            while (left >= 0 and right <= len(s)-1) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        
        for i in range(len(s)):
            
            odd = expandAroundCentre(i,i)
            even = expandAroundCentre(i,i+1)

            longer = odd if len(odd) > len(even) else even
            longest = longest if len(longest) > len(longer) else longer
        
        return longest