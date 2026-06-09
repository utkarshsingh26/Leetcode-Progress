class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)

        k = len(s1)
        window = s2[:k]
        count_window = Counter(window)

        if count_s1 == count_window:
            return True
        
        for right in range(k, len(s2)):
            
            if s2[right] in count_window:
                count_window[s2[right]] += 1
            else:
                count_window[s2[right]] = 1
            
            count_window[s2[right-k]] -= 1

            if count_s1 == count_window:
                return True
        
        return False