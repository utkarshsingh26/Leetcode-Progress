class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in range(len(s)):
            if s[i] != "#":
                stack1.append(s[i])
            elif not stack1:
                continue
            else:
                stack1.pop()
        
        for i in range(len(t)):
            if t[i] != '#':
                stack2.append(t[i])
            elif not stack2:
                continue
            else:
                stack2.pop()
        
        if stack1 == stack2:
            return True
        else:
            return False