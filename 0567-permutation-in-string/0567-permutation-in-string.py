class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)

        window = s2[:len(s1)]
        count_window = Counter(window)

        if count_window == count_s1:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            if s2[right] in count_window:
                count_window[s2[right]] += 1
            else:
                count_window[s2[right]] = 1
            
            count_window[s2[left]] -= 1
            left += 1

            if count_window == count_s1:
                return True

        return False