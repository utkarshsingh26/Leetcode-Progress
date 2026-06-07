class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack and stack[-1] != s[i]:
                stack.append(s[i])
            elif stack and stack[-1] == s[i]:
                stack.pop()
        
        return "".join(stack)