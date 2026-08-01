class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count_s1 = Counter(s1)
        
        window = s2[:len(s1)]
        count_window = Counter(window)

        if count_s1 == count_window:
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1
            
            if s2[left] in count_window:
                if count_window[s2[left]] > 0:
                    count_window[s2[left]] -= 1

                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]

            if count_s1 == count_window:
                return True

            left += 1
        
        return False