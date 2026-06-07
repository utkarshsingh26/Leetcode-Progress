class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for char in s:
            if not stack or char not in maps:
                stack.append(char)
            elif stack and char in maps and stack[-1] == maps[char]:
                stack.pop()
            elif stack and char in maps and stack[-1] != maps[char]:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
