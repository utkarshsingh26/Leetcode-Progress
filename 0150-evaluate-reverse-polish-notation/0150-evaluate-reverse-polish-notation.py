class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "/":
                    result = int(first / second)
                elif token == "*":
                    result = first * second
            
                stack.append(result)
        
        return stack[0]