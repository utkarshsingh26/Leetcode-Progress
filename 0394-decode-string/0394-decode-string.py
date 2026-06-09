class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                expanded = int(num) * string
                stack.append(expanded)
        
        return "".join(stack)
