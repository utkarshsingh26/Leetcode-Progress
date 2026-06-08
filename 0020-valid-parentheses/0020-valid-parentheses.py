class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for char in s:
            if char not in maps:
                stack.append(char)
            elif char in maps and stack and stack[-1] == maps[char]:
                stack.pop()
            elif char in maps and stack and stack[-1] != maps[char]:
                return False
            elif char in maps and not stack:
                return False
        
        if len(stack) != 0:
            return False

        return True