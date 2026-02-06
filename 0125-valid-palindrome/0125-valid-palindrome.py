class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        left = 0
        right = len(s)-1

        while left < right:
            if not (s[left] == s[right]):
                return False
            left += 1
            right -= 1
        
        return True