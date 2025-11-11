class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sett1 = set(s)
        sett2 = set(t)

        if sett1 == sett2:
            return True
        else:
            return False