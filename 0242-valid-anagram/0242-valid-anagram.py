from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1 = Counter(s)
        count2 = Counter(t)

        if count1 == count2:
            return True
        else:
            return False
