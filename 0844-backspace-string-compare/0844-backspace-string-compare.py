class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1, stack2 = [], []

        for char in s:
            if char != '#':
                stack1.append(char)
            elif char == "#" and stack1:
                stack1.pop()
        
        for char in t:
            if char != "#":
                stack2.append(char)
            elif char == "#" and stack2:
                stack2.pop()
        
        if stack1 == stack2:
            return True
        else:
            return False
