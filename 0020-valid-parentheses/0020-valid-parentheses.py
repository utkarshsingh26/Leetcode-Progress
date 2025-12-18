class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                if hashmap[char] != stack.pop():
                    return False
        
        return True if len(stack) == 0 else False