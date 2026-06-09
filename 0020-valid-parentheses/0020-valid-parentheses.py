class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for char in s:
            if not stack or char not in maps:
                stack.append(char)
            elif char in maps and stack[-1] == maps[char]:
                stack.pop()
            elif char in maps and stack[-1] != maps[char]:
                return False
           
        
        if stack:
            return False
        
        return True