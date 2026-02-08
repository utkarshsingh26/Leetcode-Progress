class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in hashmap:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                    
                if stack.pop() != hashmap[s[i]]:
                    return False
        
        return True if len(stack) == 0 else False