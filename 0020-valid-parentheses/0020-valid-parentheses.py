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
                if stack:
                    popped = stack.pop()
                    if hashmap[char] != popped:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
