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
                if not stack or stack.pop() != hashmap[s[i]]:
                    return False
        
        if stack:
            return False

        return True