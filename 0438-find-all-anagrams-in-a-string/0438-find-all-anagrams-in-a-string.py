class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        count_p = Counter(p)

        k = len(p)
        window = s[:k]
        count_window = Counter(window)

        result = []

        if count_p == count_window:
            result.append(0)

        for right in range(k, len(s)):

            if s[right] in count_window:
                count_window[s[right]] += 1
            else:
                count_window[s[right]] = 1
            
            count_window[s[right-k]] -= 1

            if count_p == count_window:
                result.append(right-k+1)
        
        return result