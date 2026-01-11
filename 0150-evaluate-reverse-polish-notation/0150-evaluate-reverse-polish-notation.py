class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    result = first + second
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = first * second
                else:
                    result = int(second/first)
                stack.append(result)
        
        return stack[-1]