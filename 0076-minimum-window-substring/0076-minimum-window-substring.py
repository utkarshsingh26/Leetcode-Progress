class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        have = 0
        need_count = len(need)
        left = 0

        result = ""
        result_len = float("inf")
        window = {}

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and need[ch] == window[ch]:
                have += 1
            
            while have == need_count:

                if (right - left + 1) < result_len:
                    result = s[left:right+1]
                    result_len = right - left + 1
                
                ch = s[left]
                window[ch] = window.get(ch, 0) - 1
                
                if ch in need and window[ch] < need[ch]:
                    have -= 1
                
                left += 1
        
        return result
        
