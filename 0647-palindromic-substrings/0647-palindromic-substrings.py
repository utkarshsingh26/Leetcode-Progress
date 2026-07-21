class Solution:
    def countSubstrings(self, s: str) -> int:
        
        max_count = 0

        def expandAroundCentre(left, right):
            count = 0
            while (left >= 0 and right <= len(s)-1) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        for i in range(len(s)):
    
            max_count += expandAroundCentre(i,i)
            max_count += expandAroundCentre(i,i+1)
        
        return max_count