class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        window = {}

        left = 0
        result = ""
        result_len = float("inf")
        
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        have = 0
        need_count = len(need)

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and need[ch] == window[ch]:
                have += 1
            
            while have == need_count:

                if (right - left + 1) < result_len:
                    result = s[left:right+1]
                    result_len = right - left + 1
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1

        return result