class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(firstNum + secondNum)
                elif token == "-":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(secondNum - firstNum)
                elif token == "*":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(firstNum * secondNum)
                elif token == "/":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(int(secondNum / firstNum))
        
        return stack[0]