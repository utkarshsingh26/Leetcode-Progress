class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        temp = []

        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start_index):
            if start_index == len(s):
                result.append(temp[:])
                return
            
            for last_index in range(start_index, len(s)):
                substring = s[start_index: last_index+1]

                if is_palindrome(substring):
                    temp.append(substring)

                    backtrack(last_index+1)

                    temp.pop()
        
        backtrack(0)
        return result