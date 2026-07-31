class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in hashmap:
                stack.append(s[i])
            else:
                
                if not stack and s[i] in hashmap:
                    return False

                if stack and stack.pop() != hashmap[s[i]]:
                    return False
        
        return True if not stack else False