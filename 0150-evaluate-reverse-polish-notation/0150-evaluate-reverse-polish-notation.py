class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        sett = {"+", "*", "/", "-"}

        for token in tokens:
            if token not in sett:
                stack.append(token)
            else:

                top = int(stack.pop())
                bottom = int(stack.pop())

                if token == "+":
                    stack.append(str(top + bottom))
                elif token == "*":
                    stack.append(str(top * bottom))
                elif token == "-":
                    stack.append(str(bottom - top))
                elif token == "/":
                    stack.append(str(int(bottom / top)))
        
        return int(stack[0])