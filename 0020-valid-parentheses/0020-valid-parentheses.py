class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for ch in s:
            if not stack or ch not in hashmap:
                stack.append(ch)
            else:
                if stack.pop() != hashmap[ch]:
                    return False
        
        return len(stack) == 0